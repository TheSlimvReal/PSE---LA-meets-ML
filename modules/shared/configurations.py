import json
from typing import Dict

from modules.controller.commands.key import Key


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
    def get_collector_config(key: Key) -> str or int:
        return Configurations.__data["collect"][Configurations.__mapping[key]]
