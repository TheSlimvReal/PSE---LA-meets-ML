from mock import patch, call

from modules.controller.controller import Controller


@patch("modules.view.command_line_interface.CommandLineInterface.print")
@patch("json.load")
@patch("builtins.input")
def test_invalid_config_file_prints_error_message(mocked_input, mocked_json, mocked_print):
    expected_calls = [
        call("InvalidConfigException: config file could not be loaded"),
        call("Finished")
    ]
    mocked_input.side_effect = ["quit"]
    mocked_json.side_effect = Exception()
    Controller().start_interaction()
    mocked_print.assert_has_calls(expected_calls)
