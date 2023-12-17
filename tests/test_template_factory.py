import os
import unittest

from rez_init.core.template_factory import TemplateFactory
from rez_init.constants import ExtensionTemplateInfo, PackageTemplateInfo


class TestTemplateFactory(unittest.TestCase):
    def test_get_default_extension_template(self):
        factory = TemplateFactory()
        self.assertEqual(
            ExtensionTemplateInfo.TEMPLATE,
            factory.get_factory_template(ExtensionTemplateInfo.KEY),
        )

    def test_get_default_package_template(self):
        factory = TemplateFactory()
        self.assertEqual(
            PackageTemplateInfo.TEMPLATE,
            factory.get_factory_template(PackageTemplateInfo.KEY),
        )

    def test_get_package_template_when_wrong_cli_type(self):
        factory = TemplateFactory()
        self.assertEqual(
            PackageTemplateInfo.TEMPLATE,
            factory.get_factory_template("wrong_type"),
        )

    def test_get_custom_extension_template(self):
        os.environ[ExtensionTemplateInfo.ENV_VAR_CUSTOM_KEY] = "custom_template"
        factory = TemplateFactory()
        self.assertEqual(
            "custom_template",
            factory.get_factory_template(ExtensionTemplateInfo.KEY),
        )
        del os.environ[ExtensionTemplateInfo.ENV_VAR_CUSTOM_KEY]

    def test_get_custom_package_template(self):
        os.environ[PackageTemplateInfo.ENV_VAR_CUSTOM_KEY] = "custom_template"
        factory = TemplateFactory()
        self.assertEqual(
            "custom_template",
            factory.get_factory_template(PackageTemplateInfo.KEY),
        )
        del os.environ[PackageTemplateInfo.ENV_VAR_CUSTOM_KEY]

    def test_get_custom_package_template_on_wrong_cli(self):
        os.environ[PackageTemplateInfo.ENV_VAR_CUSTOM_KEY] = "custom_template"
        factory = TemplateFactory()
        self.assertEqual(
            "custom_template",
            factory.get_factory_template("wrong_cli"),
        )
        del os.environ[PackageTemplateInfo.ENV_VAR_CUSTOM_KEY]
