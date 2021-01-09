# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Lead(models.Model):
    _inherit = 'crm.lead'

    branch_office = fields.Many2one('branch.office', string='Branch Office')
