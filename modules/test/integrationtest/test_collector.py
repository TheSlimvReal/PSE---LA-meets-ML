from modules.model.collector_module.collector import Collector
import h5py


def test_collect():
    data = Collector.collect(5, 128, 'unlabeled_matrices', 'modules/shared/data/')
    assert len(data) == 5
    created_file = h5py.File('modules/shared/data/unlabeled_matrices.hdf5', 'r')
    print(created_file['dense_matrices'])
