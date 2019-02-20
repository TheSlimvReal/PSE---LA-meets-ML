from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.training_module.training_module import TrainingModule


##  command to execute the training module
#
#   this command will be created when entering collect in the terminal
#   @extends Command to use its parsing logic
class TrainCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.TRAIN
        self.valid_arguments = {
            ("n", "name"): Key.NAME,
            ("p", "path"): Key.PATH,
            ("s", "saving-path"): Key.SAVING_PATH,
            ("t", "train"): Key.TRAIN,
            ("e", "existing-network"): Key.NETWORK,
            "h": Key.HELP,
        }

        self.arguments = {
            Key.NAME: None,
            Key.PATH: None,
            Key.SAVING_PATH: None,
            Key.TRAIN: None,
        }

        self.help_arguments = (
            "-p <path> Absolute path to the labeled matrices on the local storage "
            "[default: modules/shared/data/LabeledMatrices/]",
            "-n <name> Name under which the neural networks will be saved after training has finished "
            "[default: current date and time]",
            "-t <train> Float between 0 and 1. Amount of matrices used for training where 1 means all. "
            "[default: 0.8]",
            "-s <saving path> (optional) Path where the neural network state will be saved "
            "[default: modules/shared/data/NeuralNetwork/]",
        )

    def execute(self):
        super().execute()
        TrainingModule.train(
            matrices_path=self.arguments.get(Key.PATH),
            neural_network_path=self.arguments.get(Key.NETWORK),
            name=self.arguments.get(Key.NAME),
            saving_path=self.arguments.get(Key.SAVING_PATH),
            training_test_split=self.get_float_value(Key.TRAIN),
        )
