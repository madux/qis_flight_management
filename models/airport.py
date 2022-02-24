from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Airport(models.Model):
	_name = "qis.airport"
	_order = "id desc"

	name = fields.Char(string="Airport Name", required=True, help="Please enter airport name")
	location = fields.Char(string="Location", required=True, compute="compute_location", store=True)
	country_id = fields.Many2one('res.country', string="Country", required=True)

	@api.depends('name')
	def compute_location(self):
		if self.name and self.name.startswith('South Afr'):
			self.location = "Cape town"
		else:
			self.location = False




