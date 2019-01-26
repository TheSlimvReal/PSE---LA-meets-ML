from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.training_module.training_module import TrainingModule


class TrainCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.TRAIN
        self.valid_short_arguments = {
            "n": Key.NAME,
            "p": Key.PATH,
            "s": Key.SAVING_PATH,
            "t": Key.TRAIN,
            "e": Key.EXISTING_NETWORK
        }
        self.valid_long_arguments = {
            "name": Key.NAME,
            "path": Key.PATH,
            "saving-path": Key.SAVING_PATH,
            "train": Key.TRAIN,
            "existing-network": Key.EXISTING_NETWORK,
        }
        self.arguments = {
            Key.NAME: None,
            Key.PATH: None,
            Key.SAVING_PATH: None,
            Key.TRAIN: None,
            Key.EXISTING_NETWORK: None,
        }

    def execute(self):
        super().execute()
        TrainingModule.train(
            matrices_path=self.arguments.get(Key.PATH),
            neural_network_path=self.arguments.get(Key.EXISTING_NETWORK),
            name=self.arguments.get(Key.NAME),
            saving_path=self.arguments.get(Key.SAVING_PATH),
        )
