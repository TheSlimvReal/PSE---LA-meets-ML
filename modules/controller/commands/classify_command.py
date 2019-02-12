from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.classification_module.classification_module import Classifier


class ClassifyCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.CLASSIFY
        self.valid_arguments = {
            ("p", "path"): Key.PATH,
            ("n", "network"): Key.NETWORK,
            ("h", "help"): Key.HELP,
        }

        self.help_arguments = (
            "-p <path> Path to the matrix the user wants to classify [default: modules/shared/data/MatrixToClassify]",
            "-n <network> Path to the trained neural networks, if not set, uses the neural network shipped"
            "with the program [default: modules/shared/data/NeuralNetwork/]",
        )

        self.arguments = {
            Key.PATH: None,
            Key.NETWORK: None,
            Key.SOLVE: None,
        }

    def execute(self):
        super().execute()
        Classifier.start(
            self.arguments.get(Key.PATH),
            self.arguments.get(Key.NETWORK)
        )
