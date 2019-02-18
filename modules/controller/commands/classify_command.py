from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.classification_module.classification_module import Classifier


##  command to execute the classification module
#
#   this command will be created when entering classify in the command line
#   @extends Command to use its parsing logic
class ClassifyCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.CLASSIFY
        self.valid_arguments = {
            ("p", "path"): Key.PATH,
            ("n", "network"): Key.NETWORK,
            ("s", "solve"): Key.SOLVE,
            ("h", "help"): Key.HELP,
        }

        self.help_arguments = (
            "-p <path> Path to the matrix the user wants to classify",
            "-n <network> (optional) Path to the trained neural networks, if not set, uses the neural network shipped "
            "with the program",
        )

        self.arguments = {
            Key.PATH: None,
            Key.NETWORK: None,
            Key.SOLVE: None,
        }

    def execute(self):
        super().execute()
        Classifier.start(
            path=self.arguments.get(Key.PATH),
            network=self.arguments.get(Key.NETWORK)
        )
