import json
from typing import Dict

from modules.controller.commands.key import Key
from modules.controller.commands.module import Module


class Configurations:

    __mapping: Dict[Key, str] = {
        Key.AMOUNT: "amount",
        Key.NAME: "name",
        Key.PATH: "path",
        Key.SIZE: "size"
    }

    with open("config.json") as f:
        __data = json.load(f)

    @staticmethod
    def get_config(module: Module, key: Key) -> str or int:
        return Configurations.__data[module][Configurations.__mapping[key]]
