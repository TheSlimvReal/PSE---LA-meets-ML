from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.labeling_module import cl


##  command to execute the labeling process
#
#   this command will be created when entering label in the terminal
#   @extends Command to use its parsing logic
class LabelCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.LABEL
        self.valid_arguments = {
            ("n", "name"): Key.NAME,
            ("p", "path"): Key.PATH,
            ("s", "saving-path"): Key.SAVING_PATH,
            ("h", "help"): Key.HELP,
        }

        self.arguments = {
            Key.NAME: None,
            Key.PATH: None,
            Key.SIZE: None,
            Key.SAVING_PATH: None,
        }

        self.help_arguments = (
            "-p <path> (optional) Absolute path to the matrices in the local storage the user wants to have labeled "
            "[default: data/UnlabeledMatrices/default_unlabeled.hdf5]",
            "-n <name> (optional) Name under which the labeled matrices will be saved "
            "[default: \"labeled_matrices_\" + current date and time]",
            "-s <saving path> Path where the labeled matrices will be saved "
            "[default: data/LabeledMatrices/] ",
        )

    def execute(self):
        super().execute()
        cl.start(
            path=self.arguments.get(Key.PATH),
            saving_name=self.arguments.get(Key.NAME),
            saving_path=self.arguments.get(Key.SAVING_PATH)
        )
