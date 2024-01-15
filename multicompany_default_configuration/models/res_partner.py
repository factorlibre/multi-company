# © 2023 FactorLibre - Alejandro Ji Cheung <alejandro.jicheung@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, models
from odoo.tools import config


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _default_company_id(self):
        company = super()._default_company_id()
        context = self.env.context
        param = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(
                "multicompany_default_configuration.partner_default_company_enable"
            )
        )
        if (
            param == "0"
            or context.get("creating_from_company")
            or config["test_enable"]
            and not context.get("test_partner_company_default")
        ):
            return False
        return company
