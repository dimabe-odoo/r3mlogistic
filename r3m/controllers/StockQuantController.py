from odoo import http, models
from odoo.http import request
from datetime import date, timedelta


class StockQuantController(http.Controller):

    @http.route('/api/stocks', type='json', method=['GET'], cors='*')
    def get_stock(self):
        items = request.env['stock.quant'].search([('location_id.usage', '=', 'internal')], order='write_date desc')
        stocks = []
        if items:
            for item in items:
                stocks.append({
                    'pickingId': item.picking_id.id,
                    'eta': item.r3m_eta,
                    'po': item.r3m_po,
                    'container': item.r3m_container,
                    'booking': item.r3m_booking,
                    'bl': item.r3m_bl,
                    'vessel': item.r3m_vessel,
                    'pickingDate': item.r3m_picking_date,
                    'rollNumber': item.r3m_roll_number,
                    'paperType': item.r3m_paper_type,
                    'format': item.r3m_format,
                    'gramage': item.r3m_gramaje,
                    'rolWeight': item.r3m_rol_weight,
                    'linearM': item.r3m_linear_m,
                    'partnerName':item.r3m_partner_id.name,
                    'order': item.r3m_order,
                    'oc': item.r3m_oc
                })
        return stocks