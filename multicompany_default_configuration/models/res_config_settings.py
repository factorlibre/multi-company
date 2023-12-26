# © 2023 FactorLibre - Alejandro Ji Cheung <alejandro.jicheung@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    share_companies = fields.Boolean(default=False)
    share_products = fields.Boolean(default=False)

    @api.model
    def get_values(self):
        res = super().get_values()
        ir_config_sudo = self.env["ir.config_parameter"].sudo()
        partner_default_company_enable = ir_config_sudo.get_param(
            "multicompany_default_configuration.partner_default_company_enable", False
        )
        product_company_default = ir_config_sudo.get_param(
            "product_company_default.default_company_enable", False
        )
        res.update(
            share_companies=False if partner_default_company_enable == "1" else True,
            share_products=False if product_company_default == "1" else True,
        )
        return res

    def set_values(self):
        res = super().set_values()
        ir_config_sudo = self.env["ir.config_parameter"].sudo()
        ir_config_sudo.set_param(
            "multicompany_default_configuration.partner_default_company_enable",
            0 if self.share_companies else 1,
        )
        ir_config_sudo.set_param(
            "product_company_default.default_company_enable",
            0 if self.share_products else 1,
        )
        return res
