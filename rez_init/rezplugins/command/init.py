"""
Demoing Rez's command type plugin
"""

from rez.command import Command

command_behavior = {
    "hidden": False,  # (bool): default False
    "arg_mode": "passthrough",  # (str): "passthrough", "grouped", default None
}


def setup_parser(parser, completions=False):
    parser.add_argument(
        "--type",
        help="Type of package to init",
        default="package",
        choices=["package", "extension"],
    )
    parser.add_argument(
        "-t", "--template", help="Cookiecutter template used to init your package"
    )


def command(opts, parser=None, extra_arg_groups=None):
    from rez_init.core.template_factory import TemplateFactory

    factory = TemplateFactory()
    template_path = factory.get_factory_template(opts.type)

    if opts.template:
        template_path = opts.template

    factory.apply_template(template_path)


class InitCommand(Command):
    @classmethod
    def name(cls):
        return "init"


def register_plugin():
    return InitCommand
