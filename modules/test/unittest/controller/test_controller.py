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
        "notLabel -n name",
        "quit",
    ]
    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_print_error.assert_called_once()

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
    label_command = LabelCommand()
    help_tuple = label_command.help_arguments
    call_list = [call(help_text) for help_text in help_tuple]
    expected = [call("These are the possible Tags for the label-command:")] + call_list + [call("Finished")]

    mocked_input.side_effect = user_input
    con = Controller()
    con.start_interaction()
    mocked_print.assert_has_calls(expected)
    mocked_print.assert_called()
