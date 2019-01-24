from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.classification_module.classification_module import Classifier


class ClassifyCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.CLASSIFY
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
