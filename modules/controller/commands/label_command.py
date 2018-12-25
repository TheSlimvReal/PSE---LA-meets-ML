from typing import List, Dict

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.label_mode import LabelMode
from modules.exception.excpetions import IllegalArgumentException


class LabelCommand(Command):

    _valid_short_arguments = {
        "n": Key.NAME,
        "p": Key.PATH,
        "s": Key.SAVING_PATH,
    }

    _valid_long_arguments = {
        "name": Key.NAME,
        "path": Key.PATH,
        "saving-path": Key.SAVING_PATH,
    }

    _valid_modes: Dict[str, LabelMode] = {
        "label": LabelMode.LABEL,
        "add": LabelMode.ADD,
        "remove": LabelMode.REMOVE,
    }

    _mode: LabelMode
    _configs: List[str]

    def __init__(self):
        Command.__init__(self)

    def execute(self):
        if self._mode == LabelMode.LABEL:
            super().execute()
            return
        elif self._mode == LabelMode.ADD:
            [self._add_to_config(name) for name in self._configs]
        elif self._mode == LabelMode.REMOVE:
            [self._remove_from_config(name) for name in self._configs]

    def add_args(self, arg_list: List[str]) -> None:
        self._set_mode(arg_list.pop(0))
        if self._mode == LabelMode.LABEL:
            super().add_args(arg_list)
        else:
            self._configs = arg_list

    def _set_mode(self, mode: str) -> None:
        if mode in self._valid_modes:
            self._mode = self._valid_modes[mode]
        else:
            raise IllegalArgumentException("%s is not a supported mode" % mode)

    def _remove_from_config(self, name: str):
        pass

    def _add_to_config(self, name: str):
        pass
