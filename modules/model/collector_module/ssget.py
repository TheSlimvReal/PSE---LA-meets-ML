from scipy.io import loadmat
from random import randint
from collections.abc import Iterable
import os
import random
import numpy as np


##  This class handles the communication with the suit sparse matrix collection using the ssget tool
class SSGet:

    #   Use this 2 attributes if you want to do a new search in the database
    #   SEARCH_COMMAND = "ssget -s '[ @real ] && [ @rows -eq @cols ] && [ @rows -ge 129 ] && [ @rows -le 1000 ]'"
    # command for searching for all matrix ids which are squared and real
    # real_square_matrices_ids = os.popen(__SEARCH_COMMAND).read().split("\n")[:-1] #list of matrix ids

    #   use this attribute if you want to fetch your ids from an already downlaoded list
    __dir = os.getcwd()
    __real_square_matrices_ids = my_list = open('modules/model/collector_module/matrix_ids.csv', 'r').read().split("\n")

    __CUTSIZE = 128

    ##  Gets you a matrix
    #
    #   @return matrix that has been downloaded
    @staticmethod
    def get_matrix(size: int) -> np.ndarray:
        downloaded_matrix = SSGet.__download_matrix(1)
        while downloaded_matrix == []:
            downloaded_matrix = SSGet.__download_matrix(1)
        seed = randint(0, downloaded_matrix.shape[0] - SSGet.__CUTSIZE)
        return SSGet.__cut_matrix(seed, downloaded_matrix)

    @staticmethod
    def __download_matrix(size: int) -> np.ndarray:
        matrix_id = random.choice(SSGet.__real_square_matrices_ids)
        download_command = "ssget -e -i " + matrix_id + " -t mat"
        path = os.popen(download_command).read().strip()    # just an example
        if SSGet.__load(path) == []:
            return []
        else:
            return SSGet.__get_matrix_values(SSGet.__load(path)['Problem'])

    @staticmethod
    def __cut_matrix(seed: int, matrix: np.ndarray) -> np.ndarray:

        return matrix[seed:seed + SSGet.__CUTSIZE, seed:seed + SSGet.__CUTSIZE]

    @staticmethod
    def __load(path: str) -> dict:
        try:
            return loadmat(path)
        except NotImplementedError:
            # matrices in v7.3 matlab files are skipped
            return []

    @staticmethod
    def __get_matrix_values(matrix_dict: dict) -> np.ndarray:
        found = None
        todo = [matrix_dict]
        while len(todo) != 0:
            current = todo.pop(0)
            if str(type(current)) == "<class 'scipy.sparse.csc.csc_matrix'>":
                found = current
                todo = []
            elif isinstance(current, Iterable) or str(type(current)) == "<class 'numpy.void'>":
                for c in current:
                    todo.append(c)
        return found


"""
csvfile = 'matrix_ids.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in SSGet.real_square_matrices_ids:
        writer.writerow([val])
"""
