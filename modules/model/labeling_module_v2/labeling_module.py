import math

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

    SOLVER_MAP = {"bicgstab": 0, "cg": 1, "cgs": 2, "fcg": 3}

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
        LabelingModule.clean_results_folder()
        LabelingModule.__output_service.print_line(
            "Finished labeling matrices. Saved at " + saving_path + " under " + saving_name)

    @staticmethod
    def __label_dataset(dataset):

        hdf5_matrices = dataset[LabelingModule.MATRIX_KEY]
        np_matrices = np.array(hdf5_matrices, dtype=np.float64)

        matrices = []
        labels = []
        times = []

        observable: Observable = Observable()
        LabelingModule.__output_service.print_stream("Labeling matrices %s/" + str(len(np_matrices)), observable)

        for num, matrix in enumerate(np_matrices):
            csr_matrix = scipy.sparse.csr_matrix(matrix)
            matrix_name = "matrix_{}".format(num)
            save_path = LabelingModule.MTX_TMP_FOLDER + matrix_name
            scipy.io.mmwrite(save_path, csr_matrix)

            json_file = LabelingModule.create_json_file(matrix_name, save_path)

            LabelingModule.execute_benchmarks(json_file)

            label, time = LabelingModule.get_time_and_label(json_file)
            matrices.append(csr_matrix)
            labels.append(label)
            times.append(time)

            observable.next(str(num + 1))

        observable.complete()

        labeled_dataset = [matrices, labels, times]
        return labeled_dataset

    @staticmethod
    def create_json_file(matrix_name: str, save_path: str):
        json_file = LabelingModule.RESULTS_FOLDER + matrix_name + ".json"
        result_dict = [{
            "filename": os.getcwd() + "/" + save_path + ".mtx",
            "optimal": {
                "spmv": "csr"
            }
        }]
        with open(json_file, 'w') as fp:
            json.dump(result_dict, fp)
        return json_file

    @staticmethod
    def execute_benchmarks(json_file: str):
        command = ['cp', json_file, json_file + '.imd']
        subprocess.run(command)

        command = [
            LabelingModule.GINKGO_PATH + LabelingModule.SOLVER_PATH,
            '--double_buffer="' + json_file + '.bkp2"',
            '--executor="cuda"',
            '--solvers="bicgstab,cg,cgs,fcg"',
            '--max-iters=1000',
            '--rel_res_goal=1e-6',
            '<',
            '"' + json_file + '.imd"',
            '>',
            '"' + json_file + '"'
        ]
        command_string = " ".join(command)
        subprocess.Popen(command_string, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT).wait()

    @staticmethod
    def get_time_and_label(path: str):
        results_file = open(path)
        results_json = json.load(results_file)
        solvers = results_json[0]['solver']
        times = [math.inf] * len(LabelingModule.SOLVER_MAP)
        for solver in solvers:
            if solvers[solver]['completed'] is True:
                times[LabelingModule.SOLVER_MAP[solver]] = solvers[solver]['apply']['time']
        label = [0] * len(LabelingModule.SOLVER_MAP)
        if min(times) is not math.nan:
            label[times.index(min(times))] = 1

        return label, times

    @staticmethod
    def clean_results_folder():
        for file in os.listdir(LabelingModule.RESULTS_FOLDER):
            file_path = os.path.join(LabelingModule.RESULTS_FOLDER, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                LabelingModule.__output_service.prints_error(IOException(str(e)))

    ##  sets the static output service
    #
    #   use this to register your own output service at the start of the program
    #   this output service will be for called logs and results
    #   @param service OutputService that should be registered
    @staticmethod
    def set_output_service(service: OutputService):
        LabelingModule.__output_service = service
