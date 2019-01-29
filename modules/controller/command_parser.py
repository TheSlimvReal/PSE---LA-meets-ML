from typing import Dict, List

from modules.controller.commands.classify_command import ClassifyCommand
from modules.controller.commands.command import Command

from modules.controller.commands.collect_command import CollectCommand
from modules.controller.commands.help_command import HelpCommand
from modules.controller.commands.label_command import LabelCommand
from modules.controller.commands.quit_command import QuitCommand
from modules.controller.commands.train_command import TrainCommand
from modules.exception.excpetions import IllegalArgumentException


##  Class for parsing strings to a command
class CommandParser:

    __valid_commands: Dict[str, Command.__class__] = {
        "collect": CollectCommand,
        "label": LabelCommand,
        "train": TrainCommand,
        "classify": ClassifyCommand,
        "quit": QuitCommand,
        "help": HelpCommand,
    }

    @staticmethod
    def get_valid_commands() -> List[str]:
        return [key for key in CommandParser.__valid_commands]

    ##  Parses a string to a command
    #
    #   @param input_string the string that should be parsed to a command
    #   @return the command object of the specified class
    @staticmethod
    def parse_input(input_string: str) -> Command:
        arg_list = input_string.split(" ")
        mode: str = arg_list.pop(0)
        if mode in CommandParser.__valid_commands:
            command_class = CommandParser.__valid_commands[mode]
        else:
            raise IllegalArgumentException("%s is not a valid command" % mode)
        command: Command = command_class()
        command.set_args(arg_list)
        return command
