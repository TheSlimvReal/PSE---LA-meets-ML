import matplotlib.pyplot as plt

from modules.model.collector_module.collector import Collector


def test_collect():
    data = Collector.collect(5, 1, 1, "1", "1")
    assert len(data) == 5
    for matrix in data:
        plt.spy(matrix.todense())
        plt.show()

