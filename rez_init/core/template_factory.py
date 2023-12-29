import os
from rez_init.constants import ExtensionTemplateInfo, PackageTemplateInfo
from cookiecutter.main import cookiecutter


class TemplateFactory:
    INFO = {
        PackageTemplateInfo.KEY: PackageTemplateInfo,
        ExtensionTemplateInfo.KEY: ExtensionTemplateInfo,
    }

    def get_factory_template_info(self, template_type):
        return self.INFO.get(template_type, self.INFO[PackageTemplateInfo.KEY])

    def get_custom_template(self, template_type):
        info = self.get_factory_template_info(template_type)
        custom_template = os.environ.get(info.ENV_VAR_CUSTOM_KEY, None)
        return custom_template

    def apply_template(self, template, directory=None):
        cookiecutter(template, directory=directory)
