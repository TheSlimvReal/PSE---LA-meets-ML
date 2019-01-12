from modules.model.collector_module.ssget import SSGet
from modules.shared.matrix import Matrix
from modules.shared.validator import Validator


##  This class artificially creates matrices of certain size and denisty
class Generator:

    ##  Creates a matrix with the given size and density
    #
    #   @param size of the matrix
    #   @param density of the matrix
    @staticmethod
    def generate(size: int, density: float) -> Matrix:
        generated_matrix = SSGet.get_matrix(size, density)
        while not Validator.validate(generated_matrix):
            generated_matrix = SSGet.get_matrix(size, density)
        return generated_matrix
