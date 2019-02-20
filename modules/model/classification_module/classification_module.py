import numpy as np
import h5py
import keras
from h5py import File

from modules.exception.exceptions import IllegalArgumentException, IOException
from modules.shared.loader import Loader
from modules.shared.regularity_calculator import RegularityCalculator
from modules.view.output_service import OutputService


##  This class handles the classification of matrices using a neural network
class Classifier:

    __path: str = ""
    __solvers = ["Bicgstab", "Cg", "Cgs", "Fcg"]
    __output_service: OutputService = OutputService()

    ##  Starts the classification process
    #
    #   @param path where the matrix that will be classified is located
    #   @param network path where the neural network is located
    @staticmethod
    def start(path: str, network: str):
        try:
            matrix_file = Loader.load(path)
        except IOException as e:
            Classifier.__output_service.print_error(e)
            return
        try:
            Classifier.__print_prediction(matrix_file, network)
        except IllegalArgumentException as e:
            Classifier.__output_service.print_error(e)

    @staticmethod
    def __print(predictions: list):
        counter = 0
        for prediction in predictions:
            Classifier.__output_service.print_line("matrix: " + str(counter) + ", predicted solver: " + Classifier.__solvers[prediction])
            counter += 1

    ##  Load the neural network
    #
    #   @param network path where the neural network is located
    @staticmethod
    def __load_network(network: str):
        return keras.models.load_model(network)

    ##  Scales all the values of a matrix into a fixed range
    #
    #   @param matrix which will be normalized
    #   @return matrix which is normalized
    @staticmethod
    def __normalize(matrix: np.ndarray) -> np.ndarray:
        pass

    @staticmethod
    def set_output_service(service: OutputService):
        Classifier.__output_service = service

    @staticmethod
    def __check_regularity(matrix_file, key) -> bool:
        for matrix in matrix_file[key]:
            if not RegularityCalculator.is_regular(np.array(matrix, dtype=np.float64)):
                return False
        return True

    @staticmethod
    def __print_prediction(matrix_file, network):
        key = list(matrix_file.keys())[0]
        matrix = np.expand_dims(np.array(matrix_file[key], dtype=np.float64), axis=3)
        if not Classifier.check_regularity(key, matrix):
            raise IllegalArgumentException("The matrix is not regular")
        model = Classifier.__load_network(network)
        predictions = list(np.argmax(model.predict(matrix), axis=1))
        Classifier.__print(predictions)
