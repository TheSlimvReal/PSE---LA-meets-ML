import json
from typing import Dict

from modules.controller.commands.key import Key
from modules.controller.commands.module import Module


##  This class fetches default values from the config.json
class Configurations:

    __mapping: Dict[Key, str] = {
        Key.AMOUNT: "amount",
        Key.NAME: "name",
        Key.PATH: "path",
        Key.SIZE: "size",
        Key.TRAIN: "train_split",
        Key.SAVING_PATH: "saving_path",
        Key.NETWORK: "network_path",
    }

    with open("config.json") as f:
        __data = json.load(f)

    ##  Gets you a default value for the argument
    #
    #   @param module for which you want a default value
    #   @param key enum for which you want the default value
    #   @return str or int depending on the value of the .json file
    @staticmethod
    def get_config_with_key(module: Module, key: Key) -> str or int:
        return Configurations.get_config(module, Configurations.__mapping.get(key))

    ##  gets you the default value for a string
    #
    #   @param module for which you want a default value
    #   @param key string for which you want the default value
    #   @return str or int depending on the value of the .json file
    @staticmethod
    def get_config(module: Module, key: str) -> str or int:
        tag: str = module.value
        if tag in Configurations.__data:
            return Configurations.__data.get(tag).get(key)
        else:
            return None
