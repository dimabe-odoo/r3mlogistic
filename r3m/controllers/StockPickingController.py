from odoo import http, models
from odoo.http import request
from datetime import date, timedelta


class StockPickingController(http.Controller):

    @http.route('/api/receptions', type='json', method=['GET'], cors='*')
    def get_receptions(self):
        result = request.env['stock.picking'].search([('picking_type_code', '=', 'incoming')])
        recepctions = []
        if result:
            for res in result:
                recepctions.append({
                    'id': res.id,
                    'name': res.name,
                    'createdAt': res.create_date,
                    'state': res.state,
                    'parentId': res.partner_id.name,
                    'Location_Dest': res.location_dest_id.name,
                    'products': res.move_line_ids_without_package.mapped('product_id').mapped('display_name'),
                    'invoice ': res.r3m_account,
                    'order': res.r3m_order,
                    'eta': res.r3m_eta,
                    'destinationPort': res.r3m_destination.name,
                    'containerNumber': res.r3m_container,
                    'bookingNumber': res.r3m_booking,
                    'bl': res.r3m_bl,
                    'vessel': res.r3m_vessel,
                    'plantIds': res.r3m_partner_plant_ids.mapped('name'),
                    'plantId': res.r3m_plant_id.mapped('name')
                })
        return recepctions

    @http.route('/api/dispatchs', type='json', method=['GET'], cors='*')
    def get_dispatchs(self):
        result = request.env['stock.picking'].search([('picking_type_code', '=', 'outgoing')])
        dispatchs = []
        if result:
            for res in result:
                dispatchs.append({
                    'id': res.id,
                    'name': res.name,
                    'createdAt': res.create_date,
                    'state': res.state,
                    'parentId': res.partner_id.name,
                    'locationDest': res.location_dest_id.name,
                    'products': res.move_line_ids_without_package.mapped('product_id').mapped('display_name'),
                    'invoice ': res.r3m_account,
                    'order': res.r3m_order,
                    'eta': res.r3m_eta,
                    'destinationPort': res.r3m_destination.name,
                    'containerNumber': res.r3m_container,
                    'bookingNumber': res.r3m_booking,
                    'bl': res.r3m_bl,
                    'vessel': res.r3m_vessel,
                    'plantIds': res.r3m_partner_plant_ids.mapped('name'),
                    'plantId': res.r3m_plant_id.mapped('name')
                })
        return dispatchs

    @http.route('/api/picking', type='json', method=['GET'], cors='*')
    def get_picking_by_id(self,id):
        result = request.env['stock.picking'].search([('id','=',id)])
        recepctions = []
        if result:
            for res in result:
                recepctions.append({
                    'id': res.id,
                    'name': res.name,
                    'createdAt': res.create_date,
                    'state': res.state,
                    'parentId': res.partner_id.name,
                    'locationDest': res.location_dest_id.name,
                    'products': res.move_line_ids_without_package.mapped('product_id').mapped('display_name'),
                    'invoice ': res.r3m_account,
                    'order': res.r3m_order,
                    'eta': res.r3m_eta,
                    'destinationPort': res.r3m_destination.name,
                    'containerNumber': res.r3m_container,
                    'bookingNumber': res.r3m_booking,
                    'bl': res.r3m_bl,
                    'vessel': res.r3m_vessel,
                    'plantIds': res.r3m_partner_plant_ids.mapped('name'),
                    'plantId': res.r3m_plant_id.mapped('name')
                })
        return recepctions

    @http.route('/api/picking', type='json', method=['GET'], cors='*')
    def get_picking_by_name(self, name):
        result = request.env['stock.picking'].search([('name', '=', name)])
        recepctions = []
        if result:
            for res in result:
                recepctions.append({
                    'id': res.id,
                    'name': res.name,
                    'createdAt': res.create_date,
                    'state': res.state,
                    'parentId': res.partner_id.name,
                    'locationDest': res.location_dest_id.name,
                    'products': res.move_line_ids_without_package.mapped('product_id').mapped('display_name'),
                    'invoice ': res.r3m_account,
                    'order': res.r3m_order,
                    'eta': res.r3m_eta,
                    'destinationPort': res.r3m_destination.name,
                    'containerNumber': res.r3m_container,
                    'bookingNumber': res.r3m_booking,
                    'bl': res.r3m_bl,
                    'vessel': res.r3m_vessel,
                    'plantIds': res.r3m_partner_plant_ids.mapped('name'),
                    'plantId': res.r3m_plant_id.mapped('name')
                })
        return recepctions