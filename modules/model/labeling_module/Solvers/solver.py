from modules.model.labeling_module.ginkgo import Ginkgowrapper
import numpy as np


##  Abstract class representing the various solvers tht can be executed on the matrices
class Solver:

    ##  starts the solving of a matrix
    #
    #   @param ginkgo instance of Ginkgowrapper, connection to ginkgo
    #   @param matrix which will be solved
    def execute(self, ginkgo: Ginkgowrapper, matrix: np.ndarray):
        pass
