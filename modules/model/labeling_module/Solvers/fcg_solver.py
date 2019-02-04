# The class representing the fcg iterative solver

from modules.model.labeling_module.Solvers.solver import Solver
from modules.model.labeling_module.ginkgo import Ginkgowrapper
import numpy as np


class FcgSolver(Solver):

    # calculate the time it takes to solve the System Ax=b by calling the function in the c++ shared library
    #
    # @param self the instance of the class
    # @param ginkgo an instance of the class ginkgowrapper
    # @param the matrix which gets solved
    # @return the time it took to solve the system with the gmres solver
    def execute(self, ginkgo: Ginkgowrapper, matrix: np.ndarray) -> float:
        time = ginkgo.calculate_time_to_solve(matrix, 3)
        return time
