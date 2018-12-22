from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.exception.excpetions import IllegalArgumentException


class CollectorCommand(Command):

    def __init__(self):
        Command.__init__(self)

    def execute(self):
        super().execute()

    def validate(self) -> bool:
        return super().validate()

    def get_key(self, key: str) -> Key:
        if key == "-a" or key == "--amount":
            return Key.AMOUNT
        elif key == "-n" or key == "--name":
            return Key.NAME
        elif key == "-d" or key == "--density":
            return Key.DENSITY
        elif key == "-s" or key == "--size":
            return Key.SIZE
        elif key == "-p" or key == "--path":
            return Key.PATH
        else:
            raise IllegalArgumentException("Key %s is unknown" % key)
