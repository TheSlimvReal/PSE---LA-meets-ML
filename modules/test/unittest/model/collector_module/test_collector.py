import matplotlib.pyplot as plt

from modules.model.collector_module.collector import Collector


def test_collect():
    data = Collector.collect(30, 1, 1, "1", "1")
    assert len(data) == 30
    for matrix in data:
        plt.spy(matrix.todense())
        plt.show()

