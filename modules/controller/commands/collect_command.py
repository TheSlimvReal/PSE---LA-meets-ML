from typing import Dict

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key


class CollectCommand(Command):

    _valid_short_arguments: Dict[str, Key] = {
        "a": Key.AMOUNT,
        "n": Key.NAME,
        "d": Key.DENSITY,
        "p": Key.PATH,
        "s": Key.SIZE,
    }

    _valid_long_arguments: Dict[str, Key] = {
        "amount": Key.AMOUNT,
        "name": Key.NAME,
        "density": Key.DENSITY,
        "path": Key.PATH,
        "size": Key.SIZE
    }

    def execute(self):
        super().execute()
