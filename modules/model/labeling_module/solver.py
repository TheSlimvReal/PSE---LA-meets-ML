from modules.model.labeling_module.preconditioner import Preconditioner
from modules.shared.matrix import Matrix


##  Abstract class representing the various solvers tht can be executed on the matrices
class Solver:

    ##  starts the solving of a matrix
    #
    #   @param matrix which will be solved
    #   @param preconditioner which will be applied on the matrix to fasten the solving process
    def execute(self, matrix: Matrix, preconditioner: Preconditioner):
        pass
