import h5py
import numpy as np
import scipy.sparse
import scipy.io
import json
import os


class LabelingModule:

    MATRIX_KEY = "dense_matrices"
    MTX_TMP_FOLDER = "data/MtxTmpFolder/"
    RESULTS_FOLDER = "data/results/"

    @staticmethod
    def generate_matrix_files(path: str):
        hdf5_file = h5py.File(path, 'r')
        hdf5_matrices = hdf5_file[LabelingModule.MATRIX_KEY]
        np_matrices = np.array(hdf5_matrices, dtype=np.float64)

        for num, matrix in enumerate(np_matrices):
            csr_matrix = scipy.sparse.csr_matrix(matrix)
            matrix_name = "matrix_{}".format(num)
            save_path = LabelingModule.MTX_TMP_FOLDER + matrix_name
            scipy.io.mmwrite(save_path, csr_matrix)
            json_file = LabelingModule.RESULTS_FOLDER + matrix_name + ".json"
            result_dict = {
                "filename": os.getcwd() + "/" + save_path + ".mtx",
                "problem": "regular_matrix"
            }
            with open(json_file, 'w') as fp:
                json.dump(result_dict, fp)
