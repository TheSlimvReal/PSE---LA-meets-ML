from typing import Dict

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.model.collector_module.collector import Collector


class CollectCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.COLLECT
        self.valid_short_arguments: Dict[str, Key] = {
            "a": Key.AMOUNT,
            "n": Key.NAME,
            "p": Key.PATH,
            "s": Key.SIZE,
        }
        self.valid_long_arguments: Dict[str, Key] = {
            "amount": Key.AMOUNT,
            "name": Key.NAME,
            "path": Key.PATH,
            "size": Key.SIZE
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