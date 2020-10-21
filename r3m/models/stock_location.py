from odoo import fields, models


class StockLocation(models.Model):
    _inherit = 'stock.location'

    has_full_container = fields.Boolean('Almacena contenedores llenos:')
