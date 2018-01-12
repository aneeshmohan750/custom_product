# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Product Module',
    'version': '1.2',
    'category': 'Sales',
    'depends': ['base', 'decimal_precision', 'mail'],
    'description': """
Demo Module
    """,
    'data': [
        'security/custom_product_security.xml',
        'security/ir.model.access.csv',
        'wizard/custom_product_sold_view.xml',
        'views/custom_product_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
