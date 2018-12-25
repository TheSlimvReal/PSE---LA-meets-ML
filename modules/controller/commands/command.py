from typing import List, Dict
from modules.controller.commands.key import Key
from modules.exception.excpetions import IllegalArgumentException


##  Interface for the module specific commands
class Command:

    _arguments: Dict[Key, str] = {}

    _valid_short_arguments: Dict[str, Key] = {}

    _valid_long_arguments: Dict[str, Key] = {}

    _required_arguments: List[Key] = []

    @property
    def arguments(self) -> Dict[Key, str]:
        return self._arguments

    @property
    def required_arguments(self) -> List[Key]:
        return self._required_arguments

    @property
    def valid_short_arguments(self) -> Dict[str, Key]:
        return self._valid_short_arguments

    @property
    def valid_long_arguments(self) -> Dict[str, Key]:
        return self._valid_long_arguments

    ##  can be called the execute the module
    def execute(self) -> None:
        self.validate()

    ##  will be called in the command execution
    def validate(self) -> None:
        for arg in self.required_arguments:
            if arg not in self.arguments:
                raise IllegalArgumentException("%s is required" % arg)

    ## parses the string list into a dict of args
    #
    #   @param args the list retrieved by the input
    def add_args(self, arg_list: List[str]) -> None:
        args: Dict[Key, str] = {}
        while len(arg_list) != 0:
            next_key = arg_list.pop(0)
            key: Key = self._get_key(next_key)
            value: str = ""
            if not arg_list[0].startswith("-"):
                value = arg_list.pop(0)
            args[key] = value
        self._arguments = args

    def _get_key(self, next_key: str) -> Key:
        if next_key.startswith("--") and next_key[2:] in self._valid_long_arguments:
            key: Key = self.valid_long_arguments[next_key[2:]]
        elif next_key.startswith("-") and next_key[1:] in self.valid_short_arguments:
            key: Key = self.valid_short_arguments[next_key[1:]]
        else:
            raise IllegalArgumentException("%s is not a valid argument." % next_key)
        return key
