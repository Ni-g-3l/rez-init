import os


class PackageTemplateInfo:
    KEY = "package"
    TEMPLATE = "https://github.com/Ni-g-3l/rez-init/"
    ENV_VAR_CUSTOM_KEY = "REZ_INIT_CUSTOM_PACKAGE_TEMPLATE"
    DIRECTORY = os.path.join("resources", "rez-template-package")


class ExtensionTemplateInfo:
    KEY = "extension"
    TEMPLATE = "https://github.com/Ni-g-3l/rez-init/"
    ENV_VAR_CUSTOM_KEY = "REZ_INIT_CUSTOM_EXTENSION_TEMPLATE"
    DIRECTORY = os.path.join("resources", "rez-template-extension")
