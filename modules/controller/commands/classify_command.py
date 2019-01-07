from modules.controller.commands.command import Command
from modules.controller.commands.key import Key


class ClassifyCommand(Command):

    def __init__(self):
        super().__init__()
        self.valid_short_arguments = {
            "p": Key.PATH,
            "n": Key.NETWORK,
            "s": Key.SOLVE
        }
        self.valid_long_arguments = {
            "path": Key.PATH,
            "network": Key.NETWORK,
            "solve": Key.SOLVE
        }

    def execute(self):
        super().execute()
