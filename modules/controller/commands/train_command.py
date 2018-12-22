from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.exception.excpetions import IllegalArgumentException


class TrainCommand(Command):

    def __init__(self):
        Command.__init__(self)

    def execute(self):
        super().execute()

    def validate(self) -> bool:
        return super().validate()

    def get_key(self, key: str) -> Key:
        if key == "-n" or key == "--name":
            return Key.NAME
        elif key == "-p" or key == "--path":
            return Key.PATH
        elif key == "-s" or key == "--saving-path":
            return Key.SAVING_PATH
        elif key == "-t" or key == "--train":
            return Key.TRAIN
        else:
            raise IllegalArgumentException("Key %s is unknown." % key)

