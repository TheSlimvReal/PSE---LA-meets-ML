from scipy.io import loadmat
from random import randint
from collections.abc import Iterable
import os
import matplotlib.pyplot as plt
import random
import csv

from modules.shared.matrix import Matrix


##This class handles the communication with the suit sparse matrix collection using the ssget tool
class SSGet:

    #   Use this 2 attributes if you want to do a new search in the database
    #   SEARCH_COMMAND = "ssget -s '[ @real ] && [ @rows -eq @cols ] && [ @rows -ge 129 ]'" #command for searching for all matrix ids which are squared and real
    #   real_square_matrices_ids = os.popen(__SEARCH_COMMAND).read().split("\n")[:-1] #list of matrix ids

    #use this attribute if you want to fetch your ids from an already downlaoded list
    __dir = os.getcwd()
    __real_square_matrices_ids = my_list = open('modules/model/collector_module/matrix_ids.csv', 'r').read().split("\n")

    __CUTSIZE = 128

    ##  Gets you a matrix
    #
    #   @return matrix that has been downloaded
    @staticmethod
    def get_matrix(size: int, density: float) -> Matrix:
        downloaded_matrix = SSGet.__download_matrix(1)
        while not downloaded_matrix:
            downloaded_matrix = SSGet.__download_matrix(1)
        seed = randint(0, downloaded_matrix.shape[0] - SSGet.__CUTSIZE)
        print("Seed:"+str(seed))
        return SSGet.__cut_matrix(seed, downloaded_matrix)

    @staticmethod
    def __download_matrix(size: int) -> Matrix:
        matrix_id = random.choice(SSGet.__real_square_matrices_ids)
        download_command = "ssget -e -i "+matrix_id+" -t mat"
        path = os.popen(download_command).read().strip()    # just an example
        if not SSGet.__load(path):
            return []
        else:
            return SSGet.__rec(SSGet.__load(path)['Problem'])

    @staticmethod
    def __cut_matrix(seed: int, matrix: Matrix) -> Matrix:

        return matrix[seed:seed+SSGet.__CUTSIZE, seed:seed+SSGet.__CUTSIZE]

    @staticmethod
    def __load(path):
        try:
            return loadmat(path)
        except NotImplementedError:
            # matrices in v7.3 matlab files are skipped
            return []

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


"""
csvfile = 'matrix_ids.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in SSGet.real_square_matrices_ids:
        writer.writerow([val])
"""