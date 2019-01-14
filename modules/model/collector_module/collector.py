from modules.model.collector_module.generator import Generator
from modules.shared.saver import Saver


## This class handles the collecting of matrices for further use
class Collector:

    ##  Collects matrices and saves them to the specified path
    #
    #   @param amount of matrices to be created
    #   @param size of the matrices that will be created
    #   @param density of the matrices that will be created
    #   @param name of dataset under which matrices will be saved
    #   @param path where the matrices will be saved
    @staticmethod
    def collect(amount: int, size: int, density: float, name: str, path: str):
        collected_dataset = []
        for i in range(0, amount):
            matrix =  Generator.generate(size, density)
            collected_dataset.append(matrix)
        Saver.save(collected_dataset, name, path)
        return collected_dataset
