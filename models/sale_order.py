# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_branch_office(self):
        if not self.env.user.branch_office:
            raise UserError(_("Assign a branch office to the user before selling."))
        return self.env.user.branch_office.id

    partner_phone = fields.Char('Phone')
    partner_address = fields.Char('Address')
    delivery_time = fields.Char('Delivery Time')
    payment_condition = fields.Char('Payment Condition')
    branch_office = fields.Many2one('branch.office', 'Branch Office', default=_get_branch_office)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        partner_phone = ''
        partner_address = ''
        if self.partner_id:
            partner_phone = self.partner_id.phone or self.partner_id.mobile or ''
            partner_address = self.partner_id.street or self.partner_id.street2
        self.partner_phone = partner_phone
        self.partner_address = partner_address

    @api.model
    def create(self, values):
        crm_lead = self.env['crm.lead']
        res = super(SaleOrder, self).create(values)
        crm_lead_values = {
            'type': 'opportunity',
            'name': _('Sale - ') + res.partner_id.name,
            'partner_id': res.partner_id.id,
            'branch_office': res.branch_office.id,
            'planned_revenue': res.amount_total,
        }
        crm_lead.create(crm_lead_values)
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_template_id')
    def onchange_product_template_id(self):
        if self.product_template_id:
            product_id = self.env['product.product'].search([
                ('product_tmpl_id', '=', self.product_template_id.id)], limit=1)
            if product_id and self.product_id != product_id:
                self.product_id = product_id.id
