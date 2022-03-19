from odoo import models, fields, api



class Bookings_addons(models.Model):
    _inherit = "qis.booking"
    
    partner_id = fields.Many2one('res.partner', string='Customer', required=1)
    airline_id = fields.Many2one('qis.airline',string='Airline name')
    end_date = fields.Date(required=0)
    