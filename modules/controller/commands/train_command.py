from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.model.training_module.training_module import TrainingModule


class TrainCommand(Command):

    def __init__(self):
        super().__init__()
        self.valid_short_arguments = {
            "n": Key.NAME,
            "p": Key.PATH,
            "s": Key.SAVING_PATH,
            "t": Key.TRAIN,
            "h": Key.HELP,
        }

        self.valid_long_arguments = {
            "name": Key.NAME,
            "path": Key.PATH,
            "saving-path": Key.SAVING_PATH,
            "train": Key.TRAIN,
            "help": Key.HELP,
        }

        self.valid_help_arguments = {
            "-p <path> Absolute path to the labeled matrices on the local storage",
            "-n <name> Name under which the neural networks will be saved after training has finished",
            "-t <train> (optional) Float between 0 and 1. Amount of matrices used for training where 1 means all. "
            "Standard is 0.8",
            "-s <saving path> (optional) Path where the neural network state will be saved",
        }

    def execute(self):
        super().execute()
        TrainingModule.train(
            self.arguments.get(Key.PATH),
            self.arguments.get(Key.TRAIN),
            self.arguments.get(Key.Name),
            self.arguments.get(Key.SAVING_PATH),
        )
