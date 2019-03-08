from mock import patch
import h5py
import numpy as np
from modules.model.labeling_module.labeling_module import LabelingModule
from modules.model.labeling_module import cl

from random import randint

from modules.model.labeling_module.ginkgo import Ginkgowrapper



@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.__init__", return_value=None)
@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.calculate_time_to_solve", return_value=randint(0, 100))
def test_labeling_module_returns_valid_times(mocked_ginkgo_calculate, mocked_ginkgo_init):
    LabelingModule.start("UnlabeledMatrices/unlabeled_matrices.hdf5", "testLocation",
                         "modules/test/unittest/shared/data/")

    labels = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')["label_vectors"]
    times = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')["calculated_times"]

    times = np.array(times).tolist();
    index = times.index(min(times))
    assert(labels[index] == 1, "did not get the right minimum")



@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.__init__", return_value=None)
@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.calculate_time_to_solve", return_value=1)
def test_labeling_module_saves_at_the_right_location(mocked_ginkgo_calculate, mocked_ginkgo_init):
    LabelingModule.start("data/UnlabeledMatrices/unlabeled_matrices.hdf5", "testLocation",
                         "modules/test/unittest/shared/data/")

    matrices = h5py.File("data/UnlabeledMatrices/unlabeled_matrices.hdf5", 'r')["dense_matrices"]
    saved_matrices = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')["dense_matrices"]
    for i in range(len(matrices)):
        assert(np.array_equal(matrices[i], saved_matrices[i]))


@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.__init__", return_value=None)
@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.calculate_time_to_solve", return_value=1)
def test_labeling_module_each_label_is_a_vector_with_one_one_and_zeros(mocked_ginkgo_calculate, mocked_ginkgo_init):
    LabelingModule.start("data/UnlabeledMatrices/unlabeled_matrices.hdf5", "testLocation",
                         "modules/test/unittest/shared/data/")
    labels = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')["label_vectors"]

    label_list = np.array(labels).tolist()
    for label in label_list:
        assert (label.count(1) == 1), "more or less 1s than 1 in a label"
        assert (label.count(0) == len(label) - 1), "more or less 0s in a label than expected"



