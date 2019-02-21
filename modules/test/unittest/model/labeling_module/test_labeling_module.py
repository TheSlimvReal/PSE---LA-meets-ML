from mock import patch
import h5py
import numpy as np
from modules.model.labeling_module.labeling_module import LabelingModule
from modules.model.labeling_module.ginkgo import Ginkgowrapper


@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.__init__", return_value=None)
@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.calculate_time_to_solve", return_value=1)
def test_labeling_module_saves_at_the_right_location(mocked_ginkgo_calculate, mocked_ginkgo_init):
    LabelingModule.start("modules/shared/data/UnlabeledMatrices/unlabeled_matrices.hdf5", "testLocation",
                         "modules/test/unittest/shared/data/")

    file = h5py.File("modules/shared/data/UnlabeledMatrices/unlabeled_matrices.hdf5", 'r')
    saved_file = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')
    for i in range(len(file["dense_matrices"])):
        assert(np.array_equal(file["dense_matrices"][i], saved_file["dense_matrices"][i]))

