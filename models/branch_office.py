# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class BranchOffice(models.Model):
    _name = 'branch.office'
    _description = 'Branch Office'

    sequence = fields.Integer()
    name = fields.Char('Name', required=True)

    seller_ids = fields.One2many(
        'res.users', 'branch_office', string='Sellers', check_company=True,
        domain=lambda self: [('groups_id', 'in', self.env.ref('base.group_user').id)])
