from odoo import fields, models, api


class ModelName (models.Model):
    _inherit = 'product.product'

    to_confirm = fields.Boolean()
    


