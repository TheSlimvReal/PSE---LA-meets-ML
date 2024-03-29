
from mock import patch, call

from modules.model.classification_module.classification_module import Classifier
from modules.view.cli_output_service import CLIOutputService


@patch("modules.view.command_line_interface.CommandLineInterface")
@patch("modules.shared.regularity_calculator.RegularityCalculator.is_regular")
def test_classify_throws_error_if_matrix_is_irregular(mocked_validator, mocked_cli):
    Classifier.set_output_service(CLIOutputService(mocked_cli))
    mocked_validator.side_effect = [False]
    CLIOutputService(mocked_cli)
    Classifier.start("modules/test/unittest/shared/data/one_labeled_matrix.hdf5", "network")
    mocked_cli.assert_has_calls([call.print("IllegalArgumentException: The matrix is not regular")])


@patch("numpy.argmax")
@patch("modules.shared.regularity_calculator.RegularityCalculator.is_regular")
@patch("keras.models.load_model")
@patch("modules.view.command_line_interface.CommandLineInterface")
def test_matrix_is_classified_with_cg_as_result(mocked_cli, mocked_keras, mocked_validator, mocked_np):
    Classifier.set_output_service(CLIOutputService(mocked_cli))
    mocked_validator.side_effect = [True]
    CLIOutputService(mocked_cli)
    matrix_path = "modules/test/unittest/shared/data/one_labeled_matrix.hdf5"
    mocked_np.side_effect = [[1]]
    Classifier.start(matrix_path, "")
    mocked_cli.assert_has_calls([call.print("matrix: 1, predicted solver: Cg")])


@patch("numpy.argmax")
@patch("modules.shared.regularity_calculator.RegularityCalculator.is_regular")
@patch("keras.models.load_model")
@patch("modules.view.command_line_interface.CommandLineInterface")
def test_two_matrices_are_classified(mocked_cli, mocked_keras, mocked_validator, mocked_np):
    Classifier.set_output_service(CLIOutputService(mocked_cli))
    mocked_validator.side_effect = [True, True]
    CLIOutputService(mocked_cli)
    matrix_path = "modules/test/unittest/shared/data/two_labeled_matrices.hdf5"
    mocked_np.side_effect = [[1, 1]]
    Classifier.start(matrix_path, "")
    mocked_cli.assert_has_calls([
        call.print("matrix: 1, predicted solver: Cg"),
        call.print("matrix: 2, predicted solver: Cg")
    ])
