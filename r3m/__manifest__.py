# -*- coding: utf-8 -*-
{
    'name': "R3M LOGÍSTICA",

    'summary': """
        R3M LOGÍSTICA 
        """,

    'description': """
        Gestión de recursos y control de inventario
    """,

    'author': "Dimabe LTDA",
    'website': "https://www.dimabe.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'contacts', 'stock', 'sale_stock', 'purchase_stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/port.xml',
        'views/brand.xml',
        'views/truck.xml',
        'views/stock_picking.xml',
        'views/res_partner.xml',
        'views/plant.xml',
        'views/stock_quant.xml',
        'reports/delivery_slip.xml',
        'views/stock_location.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}