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
        return Configurations.__read_from_config("controller", key)

    @staticmethod
    def get_label_config(key: Key) -> str or int:
        return Configurations.__read_from_config("label", key)

    @staticmethod
    def get_train_config(key: Key) -> str or int:
        return Configurations.__read_from_config("train", key)

    @staticmethod
    def get_classify_config(key: Key) -> str or int:
        return Configurations.__read_from_config("classify", key)

    @staticmethod
    def __read_from_config(module: str, key: Key) -> str or int:
        return Configurations.__data[module][Configurations.__mapping[key]]
