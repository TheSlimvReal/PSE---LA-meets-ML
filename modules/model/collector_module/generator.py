from modules.model.collector_module.ssget import SSGet
from modules.shared.regularity_calculator import RegularityCalculator
import numpy as np


##  This class artificially creates matrices of certain size and denisty
class Generator:

    ##  Creates a matrix with the given size and density
    #
    #   @param size of the matrix
    #   @param density of the matrix
    @staticmethod
    def generate(size: int) -> np.ndarray:
        generated_matrix = SSGet.get_matrix(size)
        while not RegularityCalculator.is_regular(generated_matrix.todense()):
            generated_matrix = SSGet.get_matrix(size)
        return generated_matrix
