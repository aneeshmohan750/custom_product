# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomProductSold(models.TransientModel):
    _name = 'custom.product.sold'
    _description = 'Custom Product Sold'

    qty     = fields.Float('Quantity')

    @api.multi
    def action_custom_product_sold_apply(self):
        products = self.env['custom.product'].browse(self.env.context.get('active_ids'))
        sold_qty = products.qty - self.qty
        products.write({'qty': sold_qty})
        return products
