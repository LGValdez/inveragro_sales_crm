# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def name_get(self):
        return [(obj.id, "[%s]" % obj.default_code) for obj in self]


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def name_get(self):
        return [(obj.id, "%s" % obj.name) for obj in self]
