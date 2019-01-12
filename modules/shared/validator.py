

##  This class handles the validation of matrices
from modules.shared.matrix import Matrix
from numpy.linalg import cond


class Validator:

    __THRESHOLD = 30000


    ##  This function checks if a given matrix can be used by our program
    #
    #   @param matrix which will be checked
    @staticmethod
    def validate(matrix: Matrix) -> bool:
        if cond(matrix) > Validator.__THRESHOLD:
            return True
        else:
            return False



