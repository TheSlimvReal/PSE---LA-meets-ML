from typing import Dict

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key


class CollectorCommand(Command):

    _valid_short_arguments: Dict[str, Key] = {
        "a": Key.AMOUNT,
        "n": Key.NAME,
        "d": Key.DENSITY,
        "p": Key.PATH,
    }

    _valid_long_arguments: Dict[str, Key] = {
        "amount": Key.AMOUNT,
        "name": Key.NAME,
        "density": Key.DENSITY,
        "path": Key.PATH,
    }

    def __init__(self):
        Command.__init__(self)

    def execute(self):
        super().execute()
