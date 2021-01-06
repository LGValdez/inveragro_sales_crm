# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_phone = fields.Char('Phone')
    partner_address = fields.Char('Address')
    delivery_time = fields.Char('Delivery Time')
    payment_condition = fields.Char('Payment Condition')

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
            'name': _('Sale - ') + res.partner_id.name,
            'partner_id': res.partner_id.id,
            'planned_revenue': res.amount_total,
        }
        crm_lead.create(crm_lead_values)
        return res
