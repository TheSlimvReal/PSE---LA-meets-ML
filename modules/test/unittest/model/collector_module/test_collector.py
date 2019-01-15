import matplotlib.pyplot as plt


from modules.model.collector_module.collector import Collector
import h5py
import numpy as np

def test_collect():
    data = Collector.collect(5, 1, 1, 'unlabeled_matrices', 'modules/shared/data/')
    assert len(data) == 5
    for matrix in data:
        plt.spy(matrix.todense())
        plt.show()
    created_file = h5py.File('modules/shared/data/unlabeled_matrices.hdf5','r')
    matrix_names = list(created_file['dense_matrices'].keys())
    for name in matrix_names:
        print(np.array(created_file['dense_matrices'][name]))

