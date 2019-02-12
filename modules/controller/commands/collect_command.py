from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.collector_module.collector import Collector


class CollectCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.COLLECT
        self.valid_arguments = {
            ("a", "amount"): Key.AMOUNT,
            ("n", "name"): Key.NAME,
            ("p", "path"): Key.PATH,
            ("s", "size"): Key.SIZE,
            ("h", "help"): Key.HELP,
        }

        self.help_arguments = (
            "-a <amount> Absolute amount of matrices the user wants to generate [default: 100]",
            "-n <name> Name under which the matrices will be saved [default: current date and time]",
            "-s <size> Absolute size the generated square matrices should have. [default: 128]",
            "-p <path> Path where the created/downloaded matrices will be saved "
            "[default: modules/shared/data/UnlabeledMatrices/]",
        )

        self.arguments = {
            Key.AMOUNT: None,
            Key.NAME: None,
            Key.PATH: None,
            Key.SIZE: None
        }

    def execute(self):
        super().execute()
        Collector.collect(
            self.get_int_value(Key.AMOUNT),
            self.get_int_value(Key.SIZE),
            self.arguments.get(Key.NAME),
            self.arguments.get(Key.PATH),
        )
