from odoo import models, fields

class Plant(models.Model):
    _name = 'r3m.plant' # r3m_plant
    name = fields.Char('Nombre')
    address = fields.Char('Dirección')