from modules.controller.commands.command import Command
from modules.controller.commands.key import Key


class TrainCommand(Command):

    _valid_short_arguments = {
        "n": Key.NAME,
        "p": Key.PATH,
        "s": Key.SAVING_PATH,
        "t": Key.TRAIN,
    }

    _valid_long_arguments = {
        "name": Key.NAME,
        "path": Key.PATH,
        "saving-path": Key.SAVING_PATH,
        "train": Key.TRAIN,
    }

    def execute(self):
        super().execute()
