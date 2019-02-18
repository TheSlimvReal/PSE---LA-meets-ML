from mock import patch, call

from modules.exception.exceptions import IllegalArgumentException
from modules.view.cli_output_service import CLIOutputService
from modules.view.observable import Observable


@patch("modules.view.command_line_interface.CommandLineInterface")
def test_create_observable_to_print_three_values(mocked_cli):
    values = [
        0,
        25,
        50,
        75,
        100
    ]
    expected_calls = [call.print_overriding("downloading %s values" % str(i)) for i in values]
    obs = Observable()
    output_service = CLIOutputService(mocked_cli)
    output_service.print_stream("downloading %s values", obs)
    [obs.next(str(i)) for i in values]
    mocked_cli.assert_has_calls(expected_calls)


@patch("modules.view.command_line_interface.CommandLineInterface")
def test_print_overriding_with_incomplete_input(mocked_cli):
    values = [
        0,
        25,
        50,
        75,
        100
    ]
    expected_calls = [call.print_overriding("downloading %s" % str(i)) for i in values]
    obs = Observable()
    output_service = CLIOutputService(mocked_cli)
    output_service.print_stream("downloading", obs)
    [obs.next(str(i)) for i in values]
    mocked_cli.assert_has_calls(expected_calls)


@patch("modules.view.command_line_interface.CommandLineInterface")
def test_print_line(mocked_cli):
    outputservice = CLIOutputService(mocked_cli)
    outputservice.print_line("Hallo")
    mocked_cli.assert_has_calls([call.print("Hallo")])


@patch("modules.view.command_line_interface.CommandLineInterface")
def test_print_error(mocked_cli):
    error = IllegalArgumentException("Error")
    outputservice = CLIOutputService(mocked_cli)
    outputservice.print_error(error)
    mocked_cli.assert_has_calls([call.print(error.get_type() + ": " + "Error")])
