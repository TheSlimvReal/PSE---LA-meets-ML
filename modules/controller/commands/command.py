from typing import List, Dict
from modules.controller.commands.key import Key
from modules.exception.excpetions import IllegalArgumentException


##  Interface for the module specific commands
class Command:

    arguments: Dict[Key, str] = {}

    _valid_short_arguments: Dict[str, Key] = {}

    _valid_long_arguments: Dict[str, Key] = {}

    @property
    def valid_short_arguments(self) -> Dict[str, Key]:
        return self._valid_short_arguments

    @property
    def valid_long_arguments(self) -> Dict[str, Key]:
        return self._valid_long_arguments

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
            next_key = arg_list.pop(0)
            key: Key
            if next_key.startswith("-"):
                if next_key.startswith("--"):
                    key: Key = self.valid_long_arguments[next_key[2:]]
                else:
                    key: Key = self.valid_short_arguments[next_key[1:]]
            if not key:
                raise IllegalArgumentException("%s is not a valid argument." % next_key)
            value: str = ""
            if not arg_list[0].startswith("-"):
                value = arg_list.pop(0)
            args[key] = value
        self.arguments = args
