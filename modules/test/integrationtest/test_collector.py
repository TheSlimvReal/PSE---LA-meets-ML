from mock import patch, call

from modules.controller.controller import Controller
from modules.exception.exceptions import InvalidOSException
from modules.model.collector_module.collector import Collector
import h5py


def test_collect():
    data = Collector.collect(5, 128, 'unlabeled_matrices', 'data/')
    assert len(data) == 5
    created_file = h5py.File('data/unlabeled_matrices.hdf5', 'r')
    print(created_file['dense_matrices'])


@patch("sys.platform", "not_linux")
@patch("modules.view.command_line_interface.CommandLineInterface.print")
@patch("builtins.input")
def test_collect_with_wrong_os_prints_exception_message(mocked_input, mocked_print):
    user_input = [
        "collect -n name",
        "quit"
    ]
    expected_calls = [
        call(InvalidOSException("").get_type() + ": Collecting only works on linux with SSGet installed"),
        call("Finished")
    ]
    mocked_input.side_effect = user_input
    Controller().start_interaction()
    mocked_print.assert_has_calls(expected_calls)
