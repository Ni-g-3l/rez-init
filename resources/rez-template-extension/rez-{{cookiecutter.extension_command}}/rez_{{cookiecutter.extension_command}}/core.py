def get_message_from_{{cookiecutter.extension_command}}():
    from rez.config import config
    message = config.plugins.command.{{cookiecutter.extension_command}}.message
    return message
