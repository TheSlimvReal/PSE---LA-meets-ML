from scipy.io import loadmat
from random import randint
from collections.abc import Iterable
import os
import random
import numpy as np
import csv


##  This class handles the communication with the suit sparse matrix collection using the ssget tool
class SSGet:

    __real_square_matrices_ids = open('modules/model/collector_module/matrix_ids.csv', 'r').read().split("\n")

    ##  Gets you a matrix
    #
    #   @return matrix that has been downloaded
    @staticmethod
    def get_matrix(size: int) -> np.ndarray:
        downloaded_matrix = SSGet.__download_matrix()
        while downloaded_matrix == []:
            downloaded_matrix = SSGet.__download_matrix()
        seed = randint(0, downloaded_matrix.shape[0] - size)
        return SSGet.__cut_matrix(seed, downloaded_matrix, size)

    ##  Does a new search in the database and updates the matrix_ids.csv file
    #
    #   @return none
    @staticmethod
    def new_search() -> None:
        search_command = "ssget -s '[ @real ] && [ @rows -eq @cols ] && [ @rows -ge 129 ] && [ @rows -le 1000 ]'"
        real_square_matrices_ids = os.popen(search_command).read().split("\n")[:-1]  # list of matrix ids
        csv_file = 'matrix_ids.csv'
        with open(csv_file, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in real_square_matrices_ids:
                writer.writerow([val])
        SSGet.__real_square_matrices_ids = open('modules/model/collector_module/matrix_ids.csv', 'r').read().split("\n")

    @staticmethod
    def __download_matrix() -> np.ndarray:
        matrix_id = random.choice(SSGet.__real_square_matrices_ids)
        download_command = "ssget -e -i " + matrix_id + " -t mat 2>/dev/null"
        path = os.popen(download_command).read().strip()
        if SSGet.__load(path) == []:
            return []
        else:
            return SSGet.__get_matrix_values(SSGet.__load(path)['Problem'])

    @staticmethod
    def __cut_matrix(seed: int, matrix: np.ndarray, size: int) -> np.ndarray:
        return matrix[seed:seed + size, seed:seed + size]

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
        # breadth first search to find matrix data structure
        while len(todo) != 0:
            current = todo.pop(0)
            if SSGet.__is_matrix(current):
                # found matrix, set return value and escape loop
                found = current
                todo = []
            elif SSGet.__is_iterable(current):
                # found iterable, append values and continue loop
                todo += list(current)
        return found

    @staticmethod
    def __is_matrix(obj) -> bool:
        return str(type(obj)) == "<class 'scipy.sparse.csc.csc_matrix'>"

    @staticmethod
    def __is_iterable(obj) -> bool:
        return isinstance(obj, Iterable) or str(type(obj)) == "<class 'numpy.void'>"
