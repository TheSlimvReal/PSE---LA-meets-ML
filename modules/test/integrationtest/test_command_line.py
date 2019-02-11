from mock import patch, call

from modules.controller.controller import Controller


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
