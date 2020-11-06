from odoo import fields, models, api


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    picking_id = fields.Many2one('stock.picking')

    r3m_eta = fields.Date('ETA')

    r3m_po = fields.Char('Purchase Order')

    r3m_container = fields.Char('Contenedor')

    r3m_booking = fields.Char('Booking Number')

    r3m_bl = fields.Char('Bl')

    r3m_vessel = fields.Char('Vessel')

    r3m_picking_date = fields.Datetime('Fecha de recepcion')

    r3m_roll_number = fields.Char('N° de Rollo')

    r3m_paper_type = fields.Char('Tipo de Papel')

    r3m_format = fields.Char('Formato')

    r3m_gramaje = fields.Char('Gramaje')

    r3m_rol_weight = fields.Char('Peso Rol')

    r3m_linear_m = fields.Char('Metro Lineal')

    r3m_partner_id = fields.Many2one('res.partner', 'Proveedor')

    r3m_order = fields.Char('Pedido')

    r3m_oc = fields.Char('OC')

    @api.model
    def create(self, values_list):
        pickings = self.env['stock.picking'].search([('location_dest_id.id', '=', values_list['location_id'])])
        for picking_id in pickings:
            if picking_id and picking_id.picking_type_code == 'incoming':
                values_list['r3m_partner_id'] = picking_id.partner_id.id
                values_list['picking_id'] = picking_id.id
                values_list['r3m_eta'] = picking_id.r3m_eta
                values_list['r3m_po'] = picking_id.origin
                values_list['r3m_bl'] = picking_id.r3m_bl
                values_list['r3m_container'] = picking_id.r3m_container
                values_list['r3m_booking'] = picking_id.r3m_booking
                values_list['r3m_order'] = picking_id.r3m_order
                values_list['r3m_oc'] = picking_id.r3m_po
                values_list['r3m_picking_date'] = picking_id.date_done
                lot = self.env['stock.production.lot'].search([('id', '=', values_list['lot_id'])])
                if lot and picking_id.picking_type_code == 'incoming':
                    values_list['r3m_rol_weight'] = lot.kilos
                    values_list['r3m_linear_m'] = lot.linear_m
                values_list['r3m_gramaje'] = self.variant_search(values_list['product_id'], 'gramaje')
                values_list['r3m_paper_type'] = self.variant_search(values_list['product_id'], 'tipo de papel')
                values_list['r3m_format'] = self.variant_search(values_list['product_id'], 'formato de bobina')
        super(StockQuant, self).create(values_list)

    def charge_data(self):
        quants = self.env['stock.quant'].search([])
        for q in quants:
            pickings = self.env['stock.picking'].search([])
            lot = self.env['stock.production.lot'].search([('id', '=', q.lot_id.id)])
            for picking_id in pickings:
                if q.lot_id.id in picking_id.move_line_nosuggest_ids.mapped('lot_id').mapped('id'):
                    q.write({
                        'picking_id': picking_id.id,
                        'r3m_partner_id': picking_id.partner_id.id,
                        'r3m_eta': picking_id.r3m_eta,
                        'r3m_po': picking_id.r3m_po,
                        'r3m_vessel': picking_id.r3m_vessel,
                        'r3m_bl': picking_id.r3m_bl,
                        'r3m_container': q.lot_id.container_number,
                        'r3m_booking': picking_id.r3m_booking,
                        'r3m_rol_weight': q.lot_id.kilos,
                        'r3m_gramaje': self.variant_search(q.product_id.id, 'gramaje'),
                        'r3m_paper_type': self.variant_search(q.product_id.id, 'tipo de papel'),
                        'r3m_format': self.variant_search(q.product_id.id, 'FORMATO DE BOBINA'),
                        'r3m_linear_m': lot.linear_m,
                        'r3m_order': picking_id.r3m_order,
                        'r3m_oc': picking_id.r3m_po,
                        'r3m_picking_date': picking_id.date_done,
                    })

    def variant_search(self, product_id, variant_search):
        product = self.env['product.product'].search([('id', '=', product_id)])
        variant_res = product.product_template_attribute_value_ids.filtered(
            lambda a: a.attribute_id.name in [
                str.upper(variant_search),
                str.lower(variant_search),
                variant_search.capitalize(),
            ]
                      or a.attribute_id.name.replace(' ', '') in [
                          str.upper(variant_search.replace(' ', '')),
                          str.lower(variant_search.replace(' ', '')),
                          variant_search.capitalize().replace(' ', ''),
                      ]

        )
        if not variant_res.product_attribute_value_id:
            return ''
        variant = variant_res.product_attribute_value_id.name
        return variant

    ''.format()
