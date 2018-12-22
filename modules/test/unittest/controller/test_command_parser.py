from typing import Dict

import pytest

from modules.controller.command_parser import CommandParser
from modules.controller.commands.classify_command import ClassifyCommand
from modules.controller.commands.collector_command import CollectorCommand
from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.train_command import TrainCommand
from modules.exception.excpetions import IllegalArgumentException


def test_valid_input_returns_command():
    input_string: str = "collect"
    command: Command = CommandParser.parse_input(input_string)
    assert isinstance(command, CollectorCommand)


def test_valid_input_with_arguments():
    input_string: str = "train -p path -n name -t train -s savingPath"
    command: Command = CommandParser.parse_input(input_string)
    assert isinstance(command, TrainCommand)
    expected: Dict[Key, str] = {
        Key.PATH: "path",
        Key.NAME: "name",
        Key.TRAIN: "train",
        Key.SAVING_PATH: "savingPath"
    }
    assert command.arguments == expected


def test_valid_input_with_flag():
    input_string: str = "classify -p path -s -n network"
    command: Command = CommandParser.parse_input(input_string)
    assert isinstance(command, ClassifyCommand)
    expected: Dict[Key, str] = {
        Key.PATH: "path",
        Key.SOLVE: "",
        Key.NETWORK: "network"
    }
    assert command.arguments == expected


def test_invalid_mode_throws_exception():
    input_string: str = "labeler -n name -p path"
    with pytest.raises(IllegalArgumentException):
        CommandParser.parse_input(input_string)
