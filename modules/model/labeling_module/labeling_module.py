from modules.model.labeling_module.Solvers.cg_solver import CgSolver
from modules.model.labeling_module.Solvers.bicgstab_solver import BicgstabSolver
from modules.model.labeling_module.Solvers.fcg_solver import FcgSolver
from modules.model.labeling_module.Solvers.cgs_solver import CgsSolver
from modules.model.labeling_module.Solvers.gmres_solver import GmresSolver
from modules.view.observable import Observable
from modules.view.output_service import OutputService

from modules.shared.loader import Loader
from modules.shared.saver import Saver
from modules.model.labeling_module.ginkgo import Ginkgowrapper

import scipy.io
import scipy.sparse
import numpy as np
import h5py
import sys
from modules.view.cli_output_service import CLIOutputService
from modules.view.command_line_interface import CommandLineInterface


##  This class handles the labeling of the matrices
from modules.view.output_service import OutputService


class LabelingModule:

    __output_service: OutputService = CLIOutputService(CommandLineInterface())
    ginkgo = Ginkgowrapper
    solvers = [BicgstabSolver(), CgSolver(), CgsSolver(), FcgSolver(), GmresSolver()]

    ##  Sets up the the class for the labeling process
    #
    #   @param path where the unlabeled matrices are located
    #   @param saving_name name under which the labeled matrices will be saved
    #   @param saving_path path to where the labeled matrices will be saved
    @staticmethod
    def start(path: str, saving_name: str, saving_path: str) -> None:
        dataset_dense_format = h5py.File(path)["dense_matrices"]
        # dataset_dense_format = Loader.load(path)["dense_matrices"]

        LabelingModule.ginkgo = Ginkgowrapper(1, "reference", dataset_dense_format[0].shape[0])
        labeled_dataset = LabelingModule.__label(dataset_dense_format)
        LabelingModule.__output_service.print_line("Finished labeling matrices. Saved at " + saving_path + " under " + saving_name)
        Saver.save(labeled_dataset, saving_name, saving_path, True)

    ##  Starts the labeling process
    #
    #   @param dataset which holds matrices that will be labeled
    @staticmethod
    def __label(dataset_dense_format):

        dense_matrices = np.array(dataset_dense_format, dtype=np.float64)
        csr_matrices = []
        for matrix in dense_matrices:
            csr_matrices.append(scipy.sparse.csr_matrix(matrix))

        matrices = []
        labels = []
        observable: Observable = Observable()
        LabelingModule.__output_service.print_stream("Labeling matrices %s/" + str(len(csr_matrices)), observable)
        for i in range(len(csr_matrices)):
            label = LabelingModule.__calculate_label(csr_matrices[i])
            matrices.append(csr_matrices[i])
            labels.append(label)
            observable.next(str(i + 1))
        observable.complete()
        labeled_dataset = [matrices, labels]
        return labeled_dataset

    ##  Calculated the label for a single matrix
    #
    #   @param matrix for which a label will be created
    @staticmethod
    def __calculate_label(matrix):
        times = []
        for solver in LabelingModule.solvers:
            times.append(solver.execute(LabelingModule.ginkgo, matrix))

        label = np.array([0 for x in range(len(times))])
        label[times.index(min(times))] = 1
        return label

    @staticmethod
    def set_output_service(service: OutputService):
        LabelingModule.__output_service = service


if __name__ == "__main__":
    LabelingModule.start(sys.argv[1], sys.argv[2], sys.argv[3])
