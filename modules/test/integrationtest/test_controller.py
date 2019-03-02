from mock import patch, call

from modules.controller.controller import Controller
from modules.exception.exceptions import IllegalArgumentException


@patch("modules.controller.commands.label_command.LabelCommand.execute")
@patch("builtins.input")
def test_label_command_call(mocked_input, mocked_label):
    user_input = [
        "label -n",
        "quit"
    ]
    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_label.assert_called_once()


@patch("modules.controller.commands.collect_command.CollectCommand.execute")
@patch("builtins.input")
def test_collect_command_call(mocked_input, mocked_collect):
    user_input = [
        "collect -a",
        "quit"
    ]
    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_collect.assert_called_once()


@patch("modules.controller.commands.classify_command.ClassifyCommand.execute")
@patch("builtins.input")
def test_classify_command_call(mocked_input, mocked_classifier_command):
    user_input = [
        "classify -p path -n network",
        "quit"
    ]
    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_classifier_command.assert_called_once()


@patch("modules.controller.commands.train_command.TrainCommand.execute")
@patch("builtins.input")
def test_train_command_call(mocked_input, mocked_train):
    user_input = [
        "train -n",
        "quit"
    ]
    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_train.assert_called_once()


@patch("modules.view.command_line_interface.CommandLineInterface.print")
@patch("builtins.input")
def test_wrong_integer_format_prints_error_message(mocked_input, mocked_print):
    user_input = [
        "collect -n name -a 50.000",
        "quit"
    ]
    expected_calls = [
        call(IllegalArgumentException("").get_type() + ": 50.000 is not a integer"),
        call("Finished")
    ]
    mocked_input.side_effect = user_input
    Controller().start_interaction()
    mocked_print.assert_has_calls(expected_calls)


@patch("modules.view.command_line_interface.CommandLineInterface.print")
@patch("builtins.input")
def test_wrong_float_format_prints_error_message(mocked_input, mocked_print):
    user_input = [
        "train --train 0,72 -n name -p path",
        "quit"
    ]
    expected_calls = [
        call(IllegalArgumentException("").get_type() + ": 0,72 is not a float"),
        call("Finished")
    ]
    mocked_input.side_effect = user_input
    Controller().start_interaction()
    mocked_print.assert_has_calls(expected_calls)
