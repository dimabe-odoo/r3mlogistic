from odoo import http
from odoo.http import request


class SerialController(http.Controller):

    @http.route('/api/serial', type='json', methods=['GET'], cors="*")
    def get_serials(self):
        result = request.env['stock.production.lot'].search([])
        data = []

        if result:
            for res in result:
                data.append({
                    'Id': res.id,
                    'SerialNumber': res.name,
                    'Product' : res.product_id.display_name,
                    'Container': res.container_number,
                    'Locations': res.quant_ids.mapped('location_id').filtered(lambda a: 'Stock' in a.name).mapped(
                        'display_name'),
                    'Kilos': res.kilos,
                    'Linear_m': res.linear_m,
                    'Area_sqm': res.area_sqm
                })
        return data
