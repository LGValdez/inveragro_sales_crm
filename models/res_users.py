# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    branch_office = fields.Many2one('branch.office', string="User's Branch Office")
