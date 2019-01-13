

## This class handles the collecting of matrices for further use
from modules.model.collector_module.generator import Generator
from modules.shared.saver import Saver

import os
import numpy as np




class Collector:

    ##  Collects matrices and saves them to the specified path
    #
    #   @param amount of matrices to be created
    #   @param size of the matrices that will be created
    #   @param density of the matrices that will be created
    #   @param name of dataset under which matrices will be saved
    #   @param path where the matrices will be saved
    @staticmethod
    def collect(amount: int, size: int, density: float, name: str, path: str) -> None:
        collected_dataset = np.empty(amount)
        for i in range(0, amount):
            collected_dataset[i] = Generator.generate(size, density)
        Saver.save(collected_dataset, name, path)
