from typing import List, Dict

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.label_mode import LabelMode
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
        self.__valid_modes: Dict[str, LabelMode] = {
            "label": LabelMode.LABEL,
            "add": LabelMode.ADD,
            "remove": LabelMode.REMOVE,
        }
        self.arguments = {
            Key.NAME: None,
            Key.PATH: None,
            Key.SIZE: None,
        }

        self.valid_help_arguments = {
            "label (command) If set, enter labeling mode",
            "-p <path> Absolute path to the matrices in the local storage the user wants to have labeled",
            "-n <name> Name under which the labeled matrices will be saved",
            "-s <saving path> (optional) Path where the labeled matrices will be saved",
        }

        self.__mode: LabelMode = None
        self.__config: List[str] = []

    @property
    def mode(self) -> LabelMode:
        return self.__mode

    @property
    def config(self) -> List[str]:
        return self.__config

    def execute(self):
        if self.__mode == LabelMode.LABEL:
            super().execute()
            LabelingModule.start(
                self.arguments.get(Key.PATH),
                self.arguments.get(Key.Name),
                self.arguments.get(Key.SAVING_PATH)
            )
            return
        elif self.__mode == LabelMode.ADD:
            [self.__add_to_config(name) for name in self.__config]
        elif self.__mode == LabelMode.REMOVE:
            [self.__remove_from_config(name) for name in self.__config]

    def set_args(self, arg_list: List[str]) -> None:
        self.__set_mode(arg_list.pop(0))
        if self.__mode == LabelMode.LABEL:
            super().set_args(arg_list)
        else:
            self.__config = arg_list

    def __set_mode(self, mode: str) -> None:
        if mode in self.__valid_modes:
            self.__mode = self.__valid_modes[mode]
        else:
            raise IllegalArgumentException("%s is not a supported mode" % mode)

    def __remove_from_config(self, name: str):
        pass

    def __add_to_config(self, name: str):
        pass
