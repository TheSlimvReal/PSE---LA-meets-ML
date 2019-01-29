from typing import Dict

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.collector_module.collector import Collector


class CollectCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.COLLECT
        self.valid_arguments: Dict[str, Key] = {
            ("a", "amount"): Key.AMOUNT,
            ("n", "name"): Key.NAME,
            ("p", "path"): Key.PATH,
            ("s", "size"): Key.SIZE,
            ("h", "help"): Key.HELP,
        }

        self.help_arguments = {
            "-a Absolute amount of matrices the user wants to generate",
            "-n <name> Name under which the matrices will be saved",
            "-s <size> (optional) Absolute size the generated square matrices should have. Default is 128",
            "-p <path> (optional) Path where the created/downloaded matrices will be saved",
        }
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
