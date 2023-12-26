# © 2023 FactorLibre - Alejandro Ji Cheung <alejandro.jicheung@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        param = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(
                "multicompany_default_configuration.partner_default_company_enable"
            )
        )
        if param == "0":
            res.company_id = False
        return res
