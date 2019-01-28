import numpy as np


##  This class handles the labeling of the matrices
from modules.view.output_service import OutputService


class LabelingModule:

    __output_service: OutputService = OutputService()

    ##  Sets up the the class for the labeling process
    #
    #   @param path where the unlabeled matrices are located
    #   @param saving_name name under which the labeled matrices will be saved
    #   @param saving_path path to where the labeled matrices will be saved
    @staticmethod
    def start(path: str, saving_name: str, saving_path: str) -> None:
        pass

    ##  Starts the labeling process
    #
    #   @param dataset which holds matrices that will be labeled
    @staticmethod
    def __label(dataset):
        pass

    ##  Calculated the label for a single matrix
    #
    #   @param matrix for which a label will be created
    @staticmethod
    def __calculate_label(matrix: np.ndarray):
        pass

    @staticmethod
    def set_output_service(service: OutputService):
        LabelingModule.__output_service = service
