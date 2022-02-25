from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AirLine(models.Model):
	_name = "qis.airline"
	_order = "id desc"

	name = fields.Char(string="Airline Name", required=True, help="Please enter name")
	model = fields.Char(string="Model", required=True, placeholder="e.g Boeing")
	color = fields.Char(string="Color")
	last_maintenance_date = fields.Datetime(string="Last Maintenance Date", default=fields.Datetime.now())
	company_id = fields.Many2one('res.company', string="Company", required=True)


class Bookings(models.Model):
	_name = "qis.booking"

	ticket_num = fields.Char('Ticket Number')
	number_of_persons = fields.Integer(string="Number of Person", default=1, required=True)
	product_id = fields.Many2one('product.template', string="Product", required=True)
	amount = fields.Float(string="Amount", default=1, required=True, compute="_compute_amount")
	discount = fields.Float(string="Discount (value)", default=0)
	start_date = fields.Datetime(string="Start Date", default=fields.Datetime.now())
	end_date = fields.Datetime(string="End Date", required=True)
	status = fields.Selection(
		[('draft', 'Draft'), 
		('progress', 'Progress'), 
		('cancel', 'Cancel'),
		('done', 'Done')
		], readonly=True, default="draft", string="Status"
	)

	@api.onchange('end_date')
	def _onchange_end_date(self):
		end_date = self.end_date 
		if end_date: # bool
			if self.start_date:
				if end_date <= self.start_date:
					self.end_date = False
					raise ValidationError(f'Sorry, {end_date} cannot be greater than {self.start_date}')

	@api.depends('number_of_persons', 'product_id', 'discount')
	def _compute_amount(self):
		for rec in self:
			if rec.product_id:
				ticket_price = rec.product_id.list_price # 1000
				discount = rec.discount  # 0
				total = (ticket_price * rec.number_of_persons) - discount
				rec.amount = total
			else:
				rec.amount = False 

	def button_set_progress(self):
		self.generate_ticket_number()
		self.status = "progress"

	def button_done(self):
		self.status = "done"

	def button_cancel(self):
		self.status = "cancel"

	def generate_ticket_number(self):
		# SELECT * FROM qis_booking
		bookings = self.env['qis.booking'].search([],limit=1)
		if bookings:
			ticket = f'{bookings[-1].ticket_num}{str(self.id)}' # 009910119 + self.id
			self.ticket_num = ticket

		else:
			self.ticket_num = "000000001"

