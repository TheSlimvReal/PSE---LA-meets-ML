
from mock import patch, call

from modules.exception.exceptions import IllegalArgumentException
from modules.model.classification_module.classification_module import Classifier
from modules.view import cli_output_service
from modules.view.cli_output_service import CLIOutputService


@patch("modules.view.command_line_interface.CommandLineInterface")
@patch("modules.shared.regularity_calculator.RegularityCalculator.is_regular")
def test_classify_throws_error_if_matrix_is_irregular(mocked_validator, mocked_cli):
    Classifier.set_output_service(mocked_cli)
    mocked_validator.side_effect = [False]
    CLIOutputService(mocked_cli)
    Classifier.start("modules/test/unittest/model/classify_module/TestMatrices/test_classifier.hdf5", "network")
    mocked_cli.has_calls("IllegalArgumentException: The matrix is not regular")
