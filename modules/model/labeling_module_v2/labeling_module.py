import h5py
import numpy as np
import scipy.sparse
import scipy.io
import json
import os
import subprocess


class LabelingModule:

    MATRIX_KEY = "dense_matrices"
    MTX_TMP_FOLDER = "data/MtxTmpFolder/"
    RESULTS_FOLDER = "data/results/"
    GINKGO_PATH = os.environ["HOME"] + "/"
    SOLVER_PATH = "ginkgo/build/benchmark/solver/solver"

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
            result_dict = [{
                "filename": os.getcwd() + "/" + save_path + ".mtx",
                "optimal": {
                    "spmv": "csr"
                }
            }]
            with open(json_file, 'w') as fp:
                json.dump(result_dict, fp)

            command = ['cp', json_file, json_file + '.imd']
            subprocess.run(command)

            command = [
                LabelingModule.GINKGO_PATH + LabelingModule.SOLVER_PATH,
                '--double_buffer="' + json_file + '.bkp2"',
                '--executor="cuda"',
                '--solvers="cg,bicgstab,cgs,fcg"',
                '--max-iters=1000',
                '--rel_res_goal=1e-6',
                '<',
                '"' + json_file + '.imd"',
                '>',
                '"' + json_file + '"'
            ]
            command_string = " ".join(command)
            subprocess.Popen(command_string, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT).wait()
