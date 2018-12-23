from mock import patch, call

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
    expected_calls = [call.print_stream("downloading %s" % str(i)) for i in values]
    obs = Observable()
    output_service = CLIOutputService(mocked_cli)
    output_service.print_stream("downloading %s", obs)
    [obs.next(str(i)) for i in values]
    mocked_cli.assert_has_calls(expected_calls)
