from mock import patch, call

from modules.controller.commands.label_command import LabelCommand
from modules.controller.commands.quit_command import QuitCommand
from modules.controller.controller import Controller


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
