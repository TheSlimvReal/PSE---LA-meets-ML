from mock import patch, call
import scipy
import numpy as np

from modules.model.labeling_module import labeling_module

@patch("modules.labeling_module_ginkgo.calculate_time_to_solve")
def test_controller_with_two_iterations(mocked_ginkgo_py):
    mocked_ginkgo_py.side_effects = 3
    matrix = np.random((128,128))
    sparse_matrix = scipy.sparse.csr_matrix(matrix)
    returnV = labeling_module.calculate_label(sparse_matrix)

    print(returnV)

