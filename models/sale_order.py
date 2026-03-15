from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        vals = super()._prepare_invoice()
        if self.website_id and self.company_id.marketplace_sale_journal_id:
            vals["journal_id"] = self.company_id.marketplace_sale_journal_id.id
        return vals
