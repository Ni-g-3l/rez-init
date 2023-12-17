import os
from rez_init.constants import ExtensionTemplateInfo, PackageTemplateInfo
from cookiecutter.main import cookiecutter


class TemplateFactory:
    INFO = {
        PackageTemplateInfo.KEY: PackageTemplateInfo,
        ExtensionTemplateInfo.KEY: ExtensionTemplateInfo,
    }

    def get_factory_template(self, template_type):
        info = self.INFO.get(template_type, self.INFO[PackageTemplateInfo.KEY])
        template = os.environ.get(info.ENV_VAR_CUSTOM_KEY, info.TEMPLATE)
        return template

    def apply_template(self, template):
        cookiecutter(template)
