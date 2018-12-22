from typing import List, Dict, Tuple

from modules.controller.commands.classify_command import ClassifyCommand
from modules.controller.commands.command import Command


##  Class for parsing strings to a command
from modules.controller.commands.collector_command import CollectorCommand
from modules.controller.commands.key import Key
from modules.controller.commands.label_command import LabelCommand
from modules.controller.commands.quit_command import QuitCommand
from modules.controller.commands.train_command import TrainCommand
from modules.exception.excpetions import IllegalArgumentException


class CommandParser:

    ##  Parses a string to a command
    #
    #   @param input_string the string that should be parsed to a command
    @staticmethod
    def parse_input(input_string: str) -> Command:
        arg_list = input_string.split(" ")
        mode: str = arg_list.pop(0)
        command: Command = CommandParser._get_command(mode)
        command.add_args(arg_list)
        return command

    @staticmethod
    def _get_command(mode: str) -> Command:
        if mode == "collect":
            return CollectorCommand()
        elif mode == "label":
            return LabelCommand()
        elif mode == "train":
            return TrainCommand()
        elif mode == "classify":
            return ClassifyCommand()
        elif mode == "quit":
            return QuitCommand()
        else:
            raise IllegalArgumentException("%s is not a valid mode." % mode)
