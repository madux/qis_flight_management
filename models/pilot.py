from odoo import models, fields 
from odoo.exceptions import ValidationError


class Pilot(models.Model):
	_name = "qis.pilot"
	_inherit = "res.partner"
	_order = "id desc"

	name = fields.Char(string="Airline Name", required=True, help="Please enter name")
	graduation_date = fields.Char(string="Date of Graduation")
	company_id = fields.Many2one('res.company', string="Company", required=True)