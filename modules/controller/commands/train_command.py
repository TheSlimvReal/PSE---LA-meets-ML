from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.training_module.training_module import TrainingModule


class TrainCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.TRAIN
        self.valid_arguments = {
            ("n", "name"): Key.NAME,
            ("p", "path"): Key.PATH,
            ("s", "saving-path"): Key.SAVING_PATH,
            ("t", "train"): Key.TRAIN,
            ("e", "existing-network"): Key.EXISTING_NETWORK,
            "h": Key.HELP,
        }

        self.arguments = {
            Key.NAME: None,
            Key.PATH: None,
            Key.SAVING_PATH: None,
            Key.TRAIN: None,
            Key.EXISTING_NETWORK: None,
        }

        self.help_arguments = {
            "-p <path> Absolute path to the labeled matrices on the local storage",
            "-n <name> Name under which the neural networks will be saved after training has finished",
            "-t <train> (optional) Float between 0 and 1. Amount of matrices used for training where 1 means all. "
            "Standard is 0.8",
            "-s <saving path> (optional) Path where the neural network state will be saved",
        }

    def execute(self):
        super().execute()
        TrainingModule.train(
            matrices_path=self.arguments.get(Key.PATH),
            neural_network_path=self.arguments.get(Key.EXISTING_NETWORK),
            name=self.arguments.get(Key.NAME),
            saving_path=self.arguments.get(Key.SAVING_PATH),
        )
