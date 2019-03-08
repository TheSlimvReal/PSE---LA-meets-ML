import pytest

from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.exception.exceptions import IllegalArgumentException


def test_get_int_value_works():
    command = Command()
    command.arguments = {Key.AMOUNT: "100"}
    amount = command.get_int_value(Key.AMOUNT)
    assert isinstance(amount, int)
    assert amount == 100


def test_get_int_value_with_wrong_format_throws_exception():
    command = Command()
    command.arguments = {Key.SIZE: "20.000"}
    with pytest.raises(IllegalArgumentException):
        command.get_int_value(Key.SIZE)


def test_get_float_value_works():
    command = Command()
    command.arguments = {Key.TRAIN: "0.8"}
    train = command.get_float_value(Key.TRAIN)
    assert isinstance(train, float)
    assert train == 0.8


def test_get_float_value_with_wrong_format_throws_exception():
    command = Command()
    command.arguments = {Key.TRAIN: "0,5"}
    with pytest.raises(IllegalArgumentException):
        command.get_float_value(Key.TRAIN)
