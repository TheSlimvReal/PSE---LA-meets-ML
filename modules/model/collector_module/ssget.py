from scipy.io import loadmat
from random import randint
from collections.abc import Iterable
import os
import matplotlib.pyplot as plt

from modules.shared.matrix import Matrix


##This class handles the communication with the suit sparse matrix collection using the ssget tool
class SSGet:

    __CUTSIZE = 128
    ##  Gets you a matrix
    #
    #   @return matrix that has been downloaded
    @staticmethod
    def get_matrix(size: int, density: float) -> Matrix:
        downloaded_matrix = SSGet.__download_matrix(1)
        seed = randint(0, downloaded_matrix.shape[0] - SSGet.__CUTSIZE)
        return SSGet.__cut_matrix(seed, downloaded_matrix)

    @staticmethod
    def __download_matrix(size: int) -> Matrix:
        path = os.popen("ssget -e -i 2 -t mat").read().strip() #just an example
        print(path)
        return SSGet.__rec(SSGet.__load(path)['Problem'])

    @staticmethod
    def __cut_matrix(seed: int, matrix: Matrix) -> Matrix:
        print(str(seed)+","+str(seed+SSGet.__CUTSIZE))
        return matrix[seed:seed+SSGet.__CUTSIZE, seed:seed+SSGet.__CUTSIZE]

    @staticmethod
    def __load(path):
        try:
            return loadmat(path)
        except NotImplementedError:
            # matrices in v7.3 matlab files are skipped
            return False

    @staticmethod
    def __rec(matrix) -> Matrix:
        found = None
        todo = [matrix]
        while len(todo) != 0:
            current = todo.pop(0)
            if str(type(current)) == "<class 'scipy.sparse.csc.csc_matrix'>":
                found = current
                todo = []
            elif isinstance(current, Iterable) or str(type(current)) == "<class 'numpy.void'>":
                for c in current:
                    todo.append(c)
        return found