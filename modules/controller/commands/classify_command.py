from modules.controller.commands.command import Command
from modules.controller.commands.key import Key


class ClassifyCommand(Command):

    _valid_short_arguments = {
        "p": Key.PATH,
        "n": Key.NETWORK,
        "s": Key.SOLVE
    }

    _valid_long_arguments = {
        "path": Key.PATH,
        "network": Key.NETWORK,
        "solve": Key.SOLVE
    }

    def execute(self):
        super().execute()
