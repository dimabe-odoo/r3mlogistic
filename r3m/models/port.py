from odoo import fields, models

class Port(models.Model):
    _name = 'r3m.port'
    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string= 'Código', required= True)
    country_id = fields.Many2one(comodel_name='res.country', string = 'País')