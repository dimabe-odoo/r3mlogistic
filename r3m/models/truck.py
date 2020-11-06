from odoo import models, fields

class Truck(models.Model):
    _name = 'r3m.truck'
    name = fields.Char('Patente')
    brand = fields.Many2one(comodel_name = 'r3m.brand.truck', string = 'Marca')
    truck_model = fields.Char('Modelo')
    truck_year = fields.Integer('Año') 