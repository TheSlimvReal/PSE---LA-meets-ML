import h5py
import os
import numpy as np


##  Class that handles the saving of datasets
class Saver:

    ##  This method saves a dataset to a specified location
    #   @param dataset that will be saved(structure [[matrices],[labels]] if labeled; [matrices] if not
    #   @param name under which it will be saved
    #   @param path where it will be saved
    #   @param labeled if dataset is labeled
    @staticmethod
    def save(dataset: list, name: str, path: str, labeled: bool) -> None:
        np.seterr(all='ignore')
        path = path.replace('\\', '/')
        if not path.endswith('/'):
            path += '/'
        if not os.path.exists(path):
            os.makedirs(path)
        saving_file = h5py.File(path + name + '.hdf5', 'w')

        if labeled:
            print(dataset[0])
            dense_dataset = Saver.__to_dense_array(dataset[0])
            saving_file.create_dataset(
                'label_vectors',
                data=np.array(dataset[1], dtype=np.float64),
                compression='gzip')

            saving_file.create_dataset(
                'calculated_times',
                data=np.array(dataset[2], dtype=np.int_),
                compression='gzip'
            )
        else:
            dense_dataset = Saver.__to_dense_array(dataset)
        saving_file.create_dataset(
            'dense_matrices',
            data=dense_dataset,
            compression='gzip')

    ## This method converts a list of sparse matrices into an array of dense_matrices
    #   @param dataset of sparse matrices to be converted
    @staticmethod
    def __to_dense_array(dataset: list) -> np.ndarray:
        dense_dataset = []
        for matrix in dataset:
            dense_dataset.append(matrix.todense())
        return np.array(dense_dataset, dtype=np.float64)
