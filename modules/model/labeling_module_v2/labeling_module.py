import math

import h5py
import numpy as np
import scipy.sparse
import scipy.io
import json
import os
import subprocess

from modules.exception.exceptions import IOException
from modules.shared.loader import Loader
from modules.shared.saver import Saver
from modules.view.observable import Observable
from modules.view.output_service import OutputService


class LabelingModule:

    MATRIX_KEY = "dense_matrices"
    MTX_TMP_FOLDER = "data/MtxTmpFolder/"
    RESULTS_FOLDER = "data/results/"
    GINKGO_PATH = os.environ["HOME"] + "/"
    SOLVER_PATH = "ginkgo/build/benchmark/solver/solver"

    SOLVER_MAP = {"cg": 0, "bicgstab": 1, "cgs": 2, "fcg": 3}

    __output_service: OutputService = OutputService()

    # The starting point for the interaction with the labeling module
    #
    # The matrices will get loaded, the gingkowrapper will get initialized. After that the labeling_module
    # will proceed with the labeling. Then the labeled matrices will be safed.
    #
    # @param path where the unlabeled matrices are located
    # @param saving_name name under which the labeled matrices will be saved
    # @param saving_path path to where the labeled matrices will be saved
    @staticmethod
    def start(path: str, saving_name: str, saving_path: str) -> None:
        try:
            hdf5_file = Loader.load(path)
        except IOException as e:
            LabelingModule.__output_service.print_error(e)
            return
        labeled_dataset = LabelingModule.__label_dataset(hdf5_file)
        Saver.save(labeled_dataset, saving_name, saving_path, True)
        LabelingModule.__output_service.print_line(
            "Finished labeling matrices. Saved at " + saving_path + " under " + saving_name)

    @staticmethod
    def __label_dataset(dataset):
        hdf5_matrices = dataset[LabelingModule.MATRIX_KEY]
        np_matrices = np.array(hdf5_matrices, dtype=np.float64)

        result_dict = []
        matrices = []

        observable: Observable = Observable()
        LabelingModule.__output_service.print_stream("Preparing matrices %s/" + str(len(np_matrices)), observable)

        for num, matrix in enumerate(np_matrices):
            csr_matrix = scipy.sparse.csr_matrix(matrix)
            matrices.append(csr_matrix)

            matrix_name = "matrix_{}".format(num)
            save_path = LabelingModule.MTX_TMP_FOLDER + matrix_name
            scipy.io.mmwrite(save_path, csr_matrix)
            result_dict.append({
                "filename": os.getcwd() + "/" + save_path + ".mtx",
                "optimal": {
                    "spmv": "csr"
                }
            })
            observable.next(str(num + 1))
        observable.complete()

        json_file = LabelingModule.RESULTS_FOLDER + "results.json"
        with open(json_file, 'w') as fp:
            json.dump(result_dict, fp)

        LabelingModule.start_solver_computation(json_file)

        labels, times = LabelingModule.get_time_and_label(json_file)
        labeled_dataset = [matrices, labels, times]

        return labeled_dataset

    @staticmethod
    def start_solver_computation(json_file: str):
        command = ['cp', json_file, json_file + '.imd']
        subprocess.run(command)

        LabelingModule.__output_service.print_line("The Labeling starts now, this may take a while")

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
        LabelingModule.__output_service.print_line("Finished labeling, saving matrices to memory")


    @staticmethod
    def get_time_and_label(path: str):
        results_file = open(path)
        results_json = json.load(results_file)

        times = []
        labels = []

        for i in range(len(results_json)):
            solvers = results_json[i]['solver']
            times_vec = [math.inf] * len(LabelingModule.SOLVER_MAP)
            for solver in solvers:
                if solvers[solver]['completed'] is True:
                    times_vec[LabelingModule.SOLVER_MAP[solver]] = solvers[solver]['apply']['time']
            label_vec = [0] * len(LabelingModule.SOLVER_MAP)
            if min(times_vec) is not math.nan:
                label_vec[times_vec.index(min(times_vec))] = 1

        return labels, times

    ##  sets the static output service
    #
    #   use this to register your own output service at the start of the program
    #   this output service will be for called logs and results
    #   @param service OutputService that should be registered
    @staticmethod
    def set_output_service(service: OutputService):
        LabelingModule.__output_service = service