from typing import List, Dict

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.exception.excpetions import IllegalArgumentException
from modules.model.labeling_module.labeling_module import LabelingModule


class LabelCommand(Command):

    def __init__(self):
        super().__init__()
        self.module_name = Module.LABEL
        self.valid_short_arguments = {
            "n": Key.NAME,
            "p": Key.PATH,
            "s": Key.SAVING_PATH,
            "h": Key.HELP,
        }
        self.valid_long_arguments = {
            "name": Key.NAME,
            "path": Key.PATH,
            "saving-path": Key.SAVING_PATH,
            "help": Key.HELP,
        }

        self.arguments = {
            Key.NAME: None,
            Key.PATH: None,
            Key.SIZE: None,
        }

        self.help_arguments = {
            "-p <path> Absolute path to the matrices in the local storage the user wants to have labeled",
            "-n <name> Name under which the labeled matrices will be saved",
            "-s <saving path> (optional) Path where the labeled matrices will be saved",
        }

        self.__config: List[str] = []

    @property
    def config(self) -> List[str]:
        return self.__config

    def execute(self):
        super().execute()
        LabelingModule.start(
            self.arguments.get(Key.PATH),
            self.arguments.get(Key.NAME),
            self.arguments.get(Key.SAVING_PATH)
        )
        return
