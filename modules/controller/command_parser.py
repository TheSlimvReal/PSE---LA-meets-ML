from typing import List, Dict, Tuple

from modules.controller.commands.classify_command import ClassifyCommand
from modules.controller.commands.command import Command


##  Class for parsing strings to a command
from modules.controller.commands.collector_command import CollectorCommand
from modules.controller.commands.label_command import LabelCommand
from modules.controller.commands.quit_command import QuitCommand
from modules.controller.commands.train_command import TrainCommand
from modules.exception.excpetions import IllegalArgumentException


class CommandParser:

    _valid_commands: Dict[str, Command.__class__] = {
        "collect": CollectorCommand,
        "labeler": LabelCommand,
        "train": TrainCommand,
        "classify": ClassifyCommand,
        "quit": QuitCommand,
    }

    ##  Parses a string to a command
    #
    #   @param input_string the string that should be parsed to a command
    @staticmethod
    def parse_input(input_string: str) -> Command:
        arg_list = input_string.split(" ")
        mode: str = arg_list.pop(0)
        if mode in CommandParser._valid_commands:
            command_class = CommandParser._valid_commands[mode]
        else:
            raise IllegalArgumentException("%s is not a valid command" % mode)
        command: Command = command_class()
        command.add_args(arg_list)
        return command
