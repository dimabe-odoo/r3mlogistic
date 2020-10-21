from odoo import models, fields


class BrandTruck(models.Model):
    _name = 'r3m.brand.truck'
    name = fields.Char(string='Marca', required=True)
    logo = fields.Image(string='Logo')
