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
        except Exception:
            raise IOException("The path is not correct.")
        return matrix_file
