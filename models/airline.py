from odoo import models, fields 
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
	amount = fields.Float(string="Amount", default=1, required=True)
	discount = fields.Float(string="Discount", default=0)
