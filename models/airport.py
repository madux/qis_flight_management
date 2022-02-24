from odoo import models, fields 
from odoo.exceptions import ValidationError


class Airport(models.Model):
	_name = "qis.airport"
	_order = "id desc"

	name = fields.Char(string="Airport Name", required=True, help="Please enter airport name")
	location = fields.Char(string="Location", required=True)
	country_id = fields.Many2one('res.country', string="Country", required=True)
