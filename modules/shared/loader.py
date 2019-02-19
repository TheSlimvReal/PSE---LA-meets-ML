import numpy as np
import h5py


## Class that handles the loading of matrices
class Loader:

    ##  Loads the dataset located at the input path
    #
    #   @param path where the dataset is located
    @staticmethod
    def load(path: str) -> np.ndarray:
        matrix_file = h5py.File(path, 'r')
        key = list(matrix_file.keys())[0]
        matrix = np.expand_dims(np.array(matrix_file[key], dtype=np.float64), axis=3)
        return matrix
