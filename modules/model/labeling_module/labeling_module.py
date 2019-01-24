
from modules.shared.loader import Loader
from modules.shared.saver import Saver
from modules.model.labeling_module.ginkgo import Ginkgowrapper


import scipy.io
import scipy.sparse
import numpy as np

##  This class handles the labeling of the matrices
class LabelingModule:

    g = Ginkgowrapper(1, "reference")


    ##  Sets up the the class for the labeling process
    #
    #   @param path where the unlabeled matrices are located
    #   @param saving_name name under which the labeled matrices will be saved
    #   @param saving_path path to where the labeled matrices will be saved
    @staticmethod
    def start(path: str, saving_name: str, saving_path: str) -> None:
        dataset_dense_format = Loader.load(path)
        labeled_dataset = LabelingModule.__label(dataset_dense_format)
        Saver.save(labeled_dataset, saving_name, saving_path, True)
        print(labeled_dataset)

    ##  Starts the labeling process
    #
    #   @param dataset which holds matrices that will be labeled
    @staticmethod
    def __label(dataset):

        dense_matrices = np.array(dataset['dense_matrices'])
        csr_matrices = []
        for matrix in dense_matrices:
            csr_matrices.append(scipy.sparse.csr_matrix(matrix))

        matrices = []
        labels = []
        for matrix in csr_matrices:
            label = LabelingModule.__calculate_label(matrix)
            matrices.append(matrix)
            labels.append(label)
        labeled_dataset = [matrices, labels]
        return labeled_dataset

    ##  Calculated the label for a single matrix
    #
    #   @param matrix for which a label will be created
    @staticmethod
    def __calculate_label(matrix):
        index = LabelingModule.g.calculate_label(matrix)
        label = np.array([0,0,0,0,0])
        label[index] = 1
        return label

