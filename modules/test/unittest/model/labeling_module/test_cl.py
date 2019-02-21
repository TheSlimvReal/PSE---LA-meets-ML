from mock import patch
from modules.model.labeling_module import cl


@patch("modules.model.labeling_module.labeling_module.start", return_value=None)
def test_cl(mock_labeling_module):
    cl.start("modules/shared/data/UnlabeledMatrices/unlabeled_matrices.hdf5", "testLocation",
             "modules/test/unittest/shared/data/")


