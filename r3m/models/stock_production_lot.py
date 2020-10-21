from odoo import models, fields

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    kilos = fields.Integer('Kilos')
    linear_m = fields.Integer('Linear M')
    area_sqm = fields.Integer('AREA SQM')
    container_number = fields.Char('Número de contenedor')

    location_ids = fields.Many2many('stock.location', 'Ubicaciones', compute="compute_locations")

    to_confirm = fields.Boolean('Confirmar')

    def compute_locations(self):
        for item in self:
            item.location_ids = item.quant_ids.mapped('location_id')