from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.model.classification_module.classification_module import Classifier


class ClassifyCommand(Command):

    def __init__(self):
        super().__init__()
        self.valid_short_arguments = {
            "p": Key.PATH,
            "n": Key.NETWORK,
            "s": Key.SOLVE,
            "h": Key.HELP,
        }
        self.valid_long_arguments = {
            "path": Key.PATH,
            "network": Key.NETWORK,
            "solve": Key.SOLVE,
            "help": Key.HELP,
        }
        self.valid_help_arguments = {
            "-p <path> Path to the matrix the user wants to classify",
            "-n <network> (optional) Path to the trained neural networks, if not set, uses the neural network shipped "
            "with the program",
        }

    def execute(self):
        super().execute()
        Classifier.start(
            self.arguments.get(Key.PATH),
            self.arguments.get(Key.NETWORK)
        )
