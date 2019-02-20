import numpy as np
from numpy.linalg import det


##  This class handles the validation of matrices
class RegularityCalculator:

    ##  This function checks if a given matrix can be used by our program
    #
    #   @param matrix which will be checked
    @staticmethod
    def is_regular(matrix: np.ndarray) -> bool:
        np.seterr(all='ignore')
        if det(matrix) != 0:
            return True
        else:
            return False
