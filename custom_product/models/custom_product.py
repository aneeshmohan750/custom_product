# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.osv import expression

from odoo.addons import decimal_precision as dp

from odoo.tools import float_compare, pycompat


class ProductBrand(models.Model):
    _name = "product.brand"
    _description = "Product Brand"

    name = fields.Char('Name', index=True, required=True, translate=True)
    complete_name = fields.Char(
        'Complete Name',
        store=True)
    parent_id = fields.Many2one('product.brand', 'Parent Brand', index=True, ondelete='cascade')


    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]



class CustomProduct(models.Model):
    _name = "custom.product"
    _description = "Product"
    _order = 'id'

    name = fields.Char('Product Name')
    price = fields.Float('Price',digits=dp.get_precision('Product Price'))
    prev_price = fields.Float('Price',digits=dp.get_precision('Product Previous Price'))
    code = fields.Char('Product Code')
    prod_brand_id = fields.Many2one('product.brand', 'Product Brand', index=1)
    active = fields.Boolean('Active', default=True)
    barcode = fields.Char('Barcode')
    qty     = fields.Float('Quantity')
    _sql_constraints = [
        ('barcode_uniq', 'unique(barcode)', "A barcode can only be assigned to one product !"),
    ]

    

    @api.model
    def create(self, vals):
        product = super(CustomProduct, self.with_context(create_custom_product=True)).create(vals)
        if not(vals.get('price'))
            product.prev_price = 0.0
        else
            product.prev_price = vals.get('price')
        return product

    @api.multi
    def write(self, values):       
        res = super(CustomProduct, self).write(values)
        if 'standard_price' in values:
           res.prev_price = values['price']     
        return res

    

