from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner' # RES_PARTNER
    r3m_plant_ids = fields.Many2many(comodel_name='r3m.plant', string='Plantas')