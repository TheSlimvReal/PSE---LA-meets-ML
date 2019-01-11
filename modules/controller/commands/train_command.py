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
        }

        self.valid_long_arguments = {
            "name": Key.NAME,
            "path": Key.PATH,
            "saving-path": Key.SAVING_PATH,
            "train": Key.TRAIN,
        }

    def execute(self):
        super().execute()
        TrainingModule.train(
            self.arguments.get(Key.PATH),
            self.arguments.get(Key.TRAIN),
            self.arguments.get(Key.Name),
            self.arguments.get(Key.SAVING_PATH),
        )
