from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.exception.excpetions import IllegalArgumentException


class ClassifyCommand(Command):

    valid_short_arguments = {
        "p": Key.PATH,
        "n": Key.NETWORK,
        "s": Key.SOLVE
    }

    valid_long_arguments = {
        "path": Key.PATH,
        "network": Key.NETWORK,
        "solve": Key.SOLVE
    }

    def __init__(self):
        Command.__init__(self)

    def execute(self):
        super().execute()

    def validate(self) -> bool:
        return super().validate()

    def get_key(self, key: str) -> Key:
        if key == "-p" or key == "--path":
            return Key.PATH
        elif key == "-n" or key == "--network":
            return Key.NETWORK
        elif key == "-s" or key == "--solve":
            return Key.SOLVE
        else:
            raise IllegalArgumentException("Key %s is unknown" % key)
