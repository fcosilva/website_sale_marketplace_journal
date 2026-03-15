from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    marketplace_sale_journal_id = fields.Many2one(
        related="company_id.marketplace_sale_journal_id",
        readonly=False,
        string="Marketplace Sale Journal",
        domain="[('type', '=', 'sale'), ('company_id', '=', company_id)]",
    )
