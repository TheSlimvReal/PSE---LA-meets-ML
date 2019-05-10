import h5py
import numpy as np
import scipy.sparse
import scipy.io

class LabelingModule:

    def generate_matrix_files(self, path: str):
        hdf5_file = h5py.File(path, 'r')
        hdf5_matrices = hdf5_file['dense_matrices']
        np_matrices = np.array(hdf5_matrices, dtype=np.float64)

        for num, matrix in enumerate(np_matrices):
            csr_matrix = scipy.sparse.csr_matrix(matrix)
            scipy.io.mmwrite("matrix_{}".format(num), csr_matrix)

