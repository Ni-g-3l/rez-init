"""
{{cookiecutter.extension_description}}
"""

from rez.command import Command

# This attribute is optional, default behavior will be applied if not present.
command_behavior = {
    "hidden": False,  # (bool): default False
    "arg_mode": None,  # (str): "passthrough", "grouped", default None
}


def setup_parser(parser, completions=False):
    parser.add_argument(
        "-m", "--message", action="store_true", help="Print message from world."
    )


def command(opts, parser=None, extra_arg_groups=None):
    from rez_{{cookiecutter.extension_command}} import core

    if opts.message:
        msg = core.get_message_from_world()
        print(msg)
        return

    print("Please use '-h' flag to see what you can do to this world !")


class {{cookiecutter.extension_command.title()}}Command(Command):
    @classmethod
    def name(cls):
        return "{{cookiecutter.extension_command}}"


def register_plugin():
    return {{cookiecutter.extension_command.title()}}Command
