from modules.model.labeling_module.Solvers.solver import Solver
from modules.model.labeling_module.ginkgo import Ginkgowrapper
import numpy as np


class FcgSolver(Solver):

    def execute(self, ginkgo: Ginkgowrapper, matrix: np.ndarray) -> float:
        time = ginkgo.calculate_time_to_solve(matrix, 3)
        return time
