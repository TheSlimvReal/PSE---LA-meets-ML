from mock import patch, call

from modules.exception.exceptions import IllegalArgumentException
from modules.model.classification_module.classification_module import Classifier


@patch("modules.exception.exceptions.IllegalArgumentException")
@patch("modules.view.cli_output_service.CLIOutputService")
@patch("h5py.File")
@patch("modules.shared.regularity_calculator.RegularityCalculator.is_regular")
def test_classify_throws_error_if_matrix_is_irregular(mocked_validator, mocked_loader, mocked_cli, mocked_exception):
    Classifier.set_output_service(mocked_cli)
    mocked_validator.side_effect = [False]
    exception = IllegalArgumentException
    mocked_exception.__init__.side_effect = [exception]
    Classifier.start("path", "network")
    mocked_cli.has_calls([call.print_error(exception)])
