from mock import patch
import h5py
import numpy as np
from modules.model.labeling_module.labeling_module import LabelingModule

from random import randint


@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.__init__", return_value=None)
@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.calculate_time_to_solve", return_value=randint(0, 100))
def test_labeling_module_returns_valid_times(mocked_ginkgo_calculate, mocked_ginkgo_init):
    LabelingModule.start("modules/test/unittest/shared/data/test_unlabeled_matrices.hdf5", "testLocation",
                         "modules/test/unittest/shared/data/")

    labels = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')["label_vectors"]
    times = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')["calculated_times"]
    label_list = np.array(labels).tolist()
    for i in range(len(labels)):
        times_for_one_label = np.array(times[i]).tolist()
        index_of_fastest_solver = times_for_one_label.index(min(times_for_one_label))
        assert(label_list[i][index_of_fastest_solver] == 1.0), "did not generate the correct label"


@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.__init__", return_value=None)
@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.calculate_time_to_solve", return_value=1)
def test_labeling_module_saves_at_the_right_location(mocked_ginkgo_calculate, mocked_ginkgo_init):
    LabelingModule.start("modules/test/unittest/shared/data/test_unlabeled_matrices.hdf5", "testLocation",
                         "modules/test/unittest/shared/data/")

    matrices = h5py.File("modules/test/unittest/shared/data/test_unlabeled_matrices.hdf5", 'r')["dense_matrices"]
    saved_matrices = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')["dense_matrices"]
    for i in range(len(matrices)):
        assert(np.array_equal(matrices[i], saved_matrices[i]))


@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.__init__", return_value=None)
@patch("modules.model.labeling_module.ginkgo.Ginkgowrapper.calculate_time_to_solve", return_value=1)
def test_labeling_module_each_label_is_a_vector_with_one_one_and_zeros(mocked_ginkgo_calculate, mocked_ginkgo_init):
    LabelingModule.start("modules/test/unittest/shared/data/test_unlabeled_matrices.hdf5", "testLocation",
                         "modules/test/unittest/shared/data/")
    labels = h5py.File("modules/test/unittest/shared/data/testLocation.hdf5", 'r')["label_vectors"]

    label_list = np.array(labels).tolist()
    for label in label_list:
        assert (label.count(1) == 1), "more or less 1s than 1 in a label"
        assert (label.count(0) == len(label) - 1), "more or less 0s in a label than expected"


