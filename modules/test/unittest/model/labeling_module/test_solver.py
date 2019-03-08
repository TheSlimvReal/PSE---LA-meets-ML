import pytest

from modules.exception.exceptions import NotImplementedException
from modules.model.labeling_module.Solvers.solver import Solver


def test_solver_interface_raises_exception():
    with pytest.raises(NotImplementedException):
        Solver().execute(None, None)
