from odoo import fields, models, api


class StockQuantityHistory (models.Model):
    _inherit = 'stock.quantity.history'

    def open_at_date(self):
        super(StockQuantityHistory, self).open_at_date()
        quants = self.env['stock.quant'].search([])
        for q in quants:
            picking_id = self.env['stock.move.line'].search(
                [('lot_id.id', '=', q.lot_id.id),
                 ('product_id.id', '=', q.product_id.id)]).picking_id
            lot = self.env['stock.production.lot'].search([('id', '=', q.lot_id.id)])
            q.write({
                'picking_id': picking_id.id,
                'r3m_eta': picking_id.r3m_eta,
                'r3m_po': picking_id.r3m_po,
                'r3m_bl': picking_id.r3m_bl,
                'r3m_container': picking_id.r3m_container,
                'r3m_booking': picking_id.r3m_booking,
                'r3m_rol_weight': lot.kilos,
                'r3m_gramaje': self.variant_search(q.product_id.id, 'gramaje'),
                'r3m_paper_type': self.variant_search(q.product_id.id, 'tipo de papel'),
                'r3m_format': self.variant_search(q.product_id.id, 'formata de bobina'),
                'r3m_picking_date': picking_id.create_date,
            })
    


