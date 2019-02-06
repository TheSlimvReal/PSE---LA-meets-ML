import numpy as np
import h5py
import keras


##  This class handles the classification of matrices using a neural network
from modules.view.output_service import OutputService


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
        matrix_file = h5py.File(path, 'r')
        key = list(matrix_file.keys())[0]
        matrix = np.expand_dims(np.array(matrix_file[key], dtype=np.float64), axis=3)
        model = Classifier.__load_network(network)
        predictions = list(np.argmax(model.predict(matrix), axis=1))
        Classifier.__print(predictions)


    @staticmethod
    def __print(predictions: list):
        counter = 0
        for prediction in predictions:
            print("matrix: "+str(counter)+", predicted solver: "+Classifier.__solvers[prediction])
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
