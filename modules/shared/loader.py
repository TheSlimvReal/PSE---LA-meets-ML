import numpy as np
import h5py

from modules.exception.exceptions import IOException


## Class that handles the loading of matrices
class Loader:
    ##  Loads the dataset located at the input path
    #
    #   @param path where the dataset is located
    @staticmethod
    def load(path: str):
        try:
            matrix_file = h5py.File(path, 'r')
        except ValueError:
            raise IOException("The path is not correct.")
        key = list(matrix_file.keys())[0]
        matrix = np.expand_dims(np.array(matrix_file[key], dtype=np.float64), axis=3)
        return [matrix_file, key, matrix]
