from typing import List

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.label_mode import LabelMode
from modules.exception.excpetions import IllegalArgumentException


class LabelCommand(Command):

    mode: LabelMode
    configs: List[str]

    def __init__(self):
        Command.__init__(self)

    def execute(self):
        if self.mode == LabelMode.LABEL:
            return
        elif self.mode == LabelMode.ADD:
            [self._add_to_config(name) for name in self.configs]
        elif self.mode == LabelMode.REMOVE:
            [self._remove_from_config(name) for name in self.configs]

    def validate(self) -> bool:
        return super().validate()

    def add_args(self, arg_list: List[str]) -> None:
        self._set_mode(arg_list.pop(0))
        if self.mode == LabelMode.LABEL:
            super().add_args(arg_list)
        else:
            self.configs = arg_list

    def _set_mode(self, mode: str) -> None:
        if mode == "label":
            self.mode = LabelMode.LABEL
        elif mode == "add":
            self.mode = LabelMode.ADD
        elif mode == "remove":
            self.mode = LabelMode.REMOVE
        else:
            raise IllegalArgumentException("%s is not a supported mode" % mode)

    def get_key(self, key: str) -> Key:
        if key == "-n" or key == "--name":
            return Key.NAME
        elif key == "-p" or key == "--path":
            return Key.PATH
        elif key == "-s" or key == "--saving-path":
            return Key.SAVING_PATH
        else:
            raise IllegalArgumentException("Key %s is unknown." % key)

    def _remove_from_config(self, name: str):
        pass

    def _add_to_config(self, name: str):
        pass
