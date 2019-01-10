from collections.abc import Iterable
from scipy.io import loadmat
import os
import matplotlib.pyplot as plt
import h5py
import numpy as np




def rec(start):
    found = None
    todo = [start]
    while len(todo) != 0:
        current = todo.pop(0)
        if str(type(current)) == "<class 'scipy.sparse.csc.csc_matrix'>":
            found = current
            todo = []
        elif isinstance(current, Iterable) or str(type(current)) == "<class 'numpy.void'>":
            for c in current:
                todo.append(c)
    return found

def load(path):
    try:
        return loadmat(path)
    except NotImplementedError:
        # matrices in v7.3 matlab files are skipped
        return False





for folder in os.listdir('mat/'):
    for matrix in os.listdir('mat/' + folder + '/'):
        f = load('mat/' + folder + '/' + matrix)
        if not f:
            continue
        x = rec(f['Problem']).todense()
        plt.spy(x)
        plt.show()
