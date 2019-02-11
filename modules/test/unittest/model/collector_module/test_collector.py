import matplotlib.pyplot as plt
import pytest

from modules.model.collector_module.collector import Collector
import h5py
import numpy as np


def test_collect():
    data = Collector.collect(5, 128, 'unlabeled_matrices', 'modules/shared/data/')
    assert len(data) == 5
    #for matrix in data:
     #  plt.spy(matrix.todense())
       # plt.show()
    created_file = h5py.File('modules/shared/data/unlabeled_matrices.hdf5', 'r')
    print(created_file['dense_matrices'])

