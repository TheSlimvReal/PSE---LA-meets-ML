from typing import List, Dict
from modules.controller.commands.key import Key
from modules.exception.excpetions import IllegalArgumentException


##  Interface for the module specific commands
class Command:

    arguments: List[Key]

    def __init__(self):
        self.arguments = []

    ##  can be called the execute the module
    def execute(self) -> None:
        pass

    ##  will be called in the command construction
    def validate(self) -> bool:
        pass

    ## parses the string list into a dict of args
    #
    #   @param args the list retrieved by the input
    def add_args(self, arg_list: List[str]) -> None:
        args: Dict[Key, str] = {}
        while len(arg_list) != 0:
            key = self.get_key(arg_list.pop(0))
            value: str = ""
            if not arg_list[0].startswith("-"):
                value = arg_list.pop(0)
            args[key] = value
        self.arguments = args

    ##  Impelemnt this method in the subclass to define your valid keys
    #
    #   @param key the key that will be checked if its an argument
    def get_key(self, key: str) -> Key:
        raise IllegalArgumentException("Method not implemented")
