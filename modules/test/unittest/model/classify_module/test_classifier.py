
from mock import patch

from modules.model.classification_module.classification_module import Classifier
from modules.view.cli_output_service import CLIOutputService


@patch("modules.view.command_line_interface.CommandLineInterface")
@patch("modules.shared.regularity_calculator.RegularityCalculator.is_regular")
def test_classify_throws_error_if_matrix_is_irregular(mocked_validator, mocked_cli):
    Classifier.set_output_service(mocked_cli)
    mocked_validator.side_effect = [False]
    CLIOutputService(mocked_cli)
    Classifier.start("modules/test/unittest/model/classify_module/TestMatrices/test_classifier.hdf5", "network")
    mocked_cli.has_calls("IllegalArgumentException: The matrix is not regular")


@patch("np.argmax")
@patch("modules.shared.regularity_calculator.RegularityCalculator.is_regular")
@patch("keras.models.load_model")
@patch("modules.view.command_line_interface.CommandLineInterface")
def test_matrix_is_classified_with_cg_as_result(mocked_cli, mocked_keras, mocked_validator, mocked_np):
    Classifier.set_output_service(mocked_cli)
    mocked_validator.side_effect = [True]
    CLIOutputService(mocked_cli)
    matrix_path = "modules/test/unittest/shared/data/classify_test_matrix.hdf5"
    mocked_np.side_effect = "Cg"
    Classifier.start(matrix_path, "")
    mocked_cli.has_calls("matrix: 1, predicted solver: Cg")
