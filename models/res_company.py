from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"

    marketplace_sale_journal_id = fields.Many2one(
        "account.journal",
        string="Marketplace Sale Journal",
        help=(
            "Default sales journal used when creating invoices from e-commerce "
            "orders."
        ),
    )

    @api.constrains("marketplace_sale_journal_id")
    def _check_marketplace_sale_journal_id(self):
        for company in self:
            journal = company.marketplace_sale_journal_id
            if not journal:
                continue
            if journal.company_id != company:
                raise ValidationError(
                    _(
                        "The marketplace sale journal must belong to company "
                        "%(company)s.",
                        company=company.display_name,
                    )
                )
            if journal.type != "sale":
                raise ValidationError(
                    _("The marketplace sale journal must be a sales journal.")
                )
