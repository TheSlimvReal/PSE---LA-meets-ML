from mock import patch, call

from modules.controller.commands.label_command import LabelCommand
from modules.controller.commands.quit_command import QuitCommand
from modules.controller.controller import Controller


@patch("modules.controller.commands.quit_command.QuitCommand.execute")
@patch("modules.controller.commands.label_command.LabelCommand.execute")
@patch("modules.controller.command_parser.CommandParser.parse_input")
@patch("builtins.input")
def test_controller_with_two_iterations(mocked_input, mocked_parser, mocked_label, mocked_quit):
    user_input = [
        "label -n name",
        "quit",
    ]
    parser_return = [
        LabelCommand(),
        QuitCommand(),
    ]
    expected = [
        call("label -n name"),
        call("quit"),
    ]
    mocked_input.side_effect = user_input
    mocked_parser.side_effect = parser_return
    con = Controller()
    con.start_interaction()
    mocked_parser.assert_has_calls(expected)
    mocked_label.assert_called_once()
    mocked_quit.assert_not_called()


@patch("modules.view.cli_output_service.CLIOutputService.print_error")
@patch("builtins.input")
def test_invalid_input_calls_print_error(mocked_input, mocked_print_error):
    user_input = [
        "labeler -n name",
        "quit",
    ]
    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_print_error.assert_called_once()


@patch("modules.view.cli_output_service.CLIOutputService.print_error")
@patch("modules.view.cli_output_service.CLIOutputService.print_line")
@patch("builtins.input")
def test_input_calls_with_two_spaces(mocked_input, mocked_print_line, mocked_print_error):
    user_input = [
        "label  -n name",
        "quit",
    ]
    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_print_line.assert_called()
    mocked_print_error.assert_not_called()


@patch("modules.model.collector_module.ssget.SSGet.new_search")
@patch("builtins.input")
def test_ssget_update_command_calls_new_search(mocked_input, mocked_search):
    user_input = [
        "ssget -u",
        "quit"
    ]
    mocked_input.side_effect = user_input
    Controller().start_interaction()
    mocked_search.assert_called()


@patch("modules.view.cli_output_service.CLIOutputService.print_line")
@patch("builtins.input")
def test_help_flag_print(mocked_input, mocked_print):
    user_input = [
        "label -h",
        "quit",
    ]
    expected2 = [
        call("These are the possible Tags for the label-command:"),
        call("-p <path> Absolute path to the matrices in the local storage the user wants to have labeled"),
        call("-n <name> Name under which the labeled matrices will be saved"),
        call("-s <saving path> (optional) Path where the labeled matrices will be saved"),
        call("Finished"),
    ]
    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_print.assert_has_calls(expected2)
    mocked_print.assert_called()
