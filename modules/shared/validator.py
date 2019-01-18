

##  This class handles the validation of matrices
from modules.shared.matrix import Matrix
from numpy.linalg import det


class Validator:

    __THRESHOLD = 30000


    ##  This function checks if a given matrix can be used by our program
    #
    #   @param matrix which will be checked
    @staticmethod
    def validate(matrix: Matrix) -> bool:
        if det(matrix) != 0:
            return True
        else:
            return False



