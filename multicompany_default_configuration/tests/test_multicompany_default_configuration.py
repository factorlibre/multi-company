# © 2023 FactorLibre - Alejandro Ji Cheung <alejandro.jicheung@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.tests import common, tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestMultiCompanyDefaultConfiguration(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(
            context=dict(
                cls.env.context,
                mail_create_nolog=True,
                mail_create_nosubscribe=True,
                mail_notrack=True,
                no_reset_password=True,
                tracking_disable=True,
            )
        )

        cls.config = cls.env["res.config.settings"].create(
            {
                "share_products": True,
                "share_companies": True,
            }
        )
        cls.config.execute()

    @mute_logger("odoo.models", "odoo.models.unlink", "odoo.addons.base.ir.ir_model")
    def test_multi_company_shared_objects(self):
        ir_config_sudo = self.env["ir.config_parameter"].sudo()

        # set configuration to False so that products and companies are not shared
        self.config.write({"share_products": False, "share_companies": False})
        self.config.execute()
        share_companies = ir_config_sudo.get_param(
            "product_company_default.default_company_enable"
        )
        share_products = ir_config_sudo.get_param(
            "multicompany_default_configuration.partner_default_company_enable"
        )
        self.assertEqual(share_companies, "1")
        self.assertEqual(share_products, "1")

        # create a partner and check the field company_id
        partner = self.env["res.partner"].create({"name": "Partner 1"})
        self.assertNotEqual(partner.company_id, False)

        # create a product and check the field company_id
        product = self.env["product.product"].create({"name": "Product Test 1"})
        self.assertNotEqual(product.company_id, False)

        # set configuration to True so that products and companies are shared
        self.config.write({"share_products": True, "share_companies": True})
        self.config.execute()
        share_companies = ir_config_sudo.get_param(
            "product_company_default.default_company_enable"
        )
        share_products = ir_config_sudo.get_param(
            "multicompany_default_configuration.partner_default_company_enable"
        )
        self.assertEqual(share_companies, "0")
        self.assertEqual(share_products, "0")

        # create a partner and check the field company_id
        partner = self.env["res.partner"].create({"name": "Partner 2"})
        self.assertEqual(partner.company_id.id, False)

        # create a product and check the field company_id
        product = self.env["product.product"].create({"name": "Product Test 2"})
        self.assertEqual(product.company_id.id, False)
