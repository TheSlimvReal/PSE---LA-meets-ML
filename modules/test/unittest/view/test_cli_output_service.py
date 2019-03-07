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
    output_service = CLIOutputService(mocked_cli)
    output_service.print_line("Hallo")
    mocked_cli.assert_has_calls([call.print("Hallo")])


@patch("modules.view.command_line_interface.CommandLineInterface")
def test_print_error(mocked_cli):
    error = IllegalArgumentException("Error")
    output_service = CLIOutputService(mocked_cli)
    output_service.print_error(error)
    mocked_cli.assert_has_calls([call.print(error.get_type() + ": " + "Error")])


@patch("modules.view.cli_output_service.CLIOutputService")
def test_removing_subscribers_from_observable_works(mocked_output_service):
    expected_calls = [
        call.update("printed"),
        call.finished()
    ]
    obs = Observable()
    obs.add_subscriber(mocked_output_service)
    obs.next("printed")
    obs.remove_subscriber(mocked_output_service)
    obs.next("not displayed")
    mocked_output_service.assert_has_calls(expected_calls)
