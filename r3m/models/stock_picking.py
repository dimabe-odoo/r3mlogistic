# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    r3m_po = fields.Char('Purchase Order')
    r3m_order = fields.Char('Pedido')
    r3m_destination = fields.Many2one(comodel_name='r3m.port', string='Puerto destino')
    r3m_container = fields.Char('Contenedor')
    r3m_booking = fields.Char('Booking Number')
    r3m_bl = fields.Char('BL')
    r3m_vessel = fields.Char('Vessel')
    r3m_account = fields.Char('Factura')
    r3m_partner_plant_ids = fields.Many2many('r3m.plant', related='partner_id.r3m_plant_ids')
    r3m_plant_id = fields.Many2one('r3m.plant', string='Planta')
    r3m_eta = fields.Date('ETA')

    remarks = fields.Text('Observaciones')

    # Transporte 

    r3m_truck = fields.Many2one(comodel_name='r3m.truck', string='Camión')
    r3m_driver = fields.Many2one(comodel_name='res.partner', string='Conductor')
    r3m_date_dispatched = fields.Datetime('Fecha de salida')
    r3m_date_on_port = fields.Datetime('Fecha llegada a destino')

    confirmed_container = fields.Char('Ingrese contenedor')

    has_full_container = fields.Boolean(compute='compute_has_full_container')

    lot_products_ids = fields.Many2many(comodel_name='stock.production.lot', string='Productos')

    @api.onchange('location_id')
    def compute_has_full_container(self):
        for item in self:
            item.has_full_container = item.location_id.has_full_container

    def check_container(self):
        if not self.confirmed_container or self.confirmed_container == '':
            raise models.ValidationError('Debe ingregar el numero del contenedor')
        if self.lot_products_ids:
            self.write({
                'lot_products_ids' : [(5)]
            })
        products = self.env['stock.production.lot'].search(
            [('container_number', 'like', self.confirmed_container)]).filtered(
            lambda a: self.location_id in a.quant_ids.mapped('location_id') and a.quant_ids.mapped(
                'location_id').filtered(lambda b: b.has_full_container))
        for pro in products:
            self.write({
                'lot_products_ids': [
                    (4, pro.id)
                ]
            })

    def confirmed_product(self):
        for product in self.lot_products_ids:
            if product.to_confirm:
                stock_move = self.env['stock.move'].create({
                    'company_id': self.env.user.company_id.id,
                    'picking_id': self.id,
                    'product_id': product.product_id.id,
                    'date': datetime.datetime.now(),
                    'date_expected': datetime.datetime.now(),
                    'location_id': self.location_id.id,
                    'location_dest_id': self.location_dest_id.id,
                    'name': self.name,
                    'state': 'draft',
                    'procure_method': 'make_to_stock',
                    'product_uom': product.product_id.uom_id.id
                })
                self.env['stock.move.line'].create({
                    'company_id': self.env.user.company_id.id,
                    'move_id': stock_move.id,
                    'picking_id': self.id,
                    'product_id': product.product_id.id,
                    'lot_id': product.id,
                    'state': 'draft',
                    'date': datetime.datetime.now(),
                    'location_id': self.location_id.id,
                    'location_dest_id': self.location_dest_id.id,
                    'product_uom_id': product.product_id.uom_id.id
                })
                self.write({
                    'lot_products_ids': [
                        (3, product.id)
                    ]
                })
