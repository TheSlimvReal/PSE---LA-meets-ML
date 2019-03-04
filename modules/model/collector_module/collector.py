from modules.model.collector_module.generator import Generator
from modules.shared.saver import Saver
from modules.view.observable import Observable
from modules.view.output_service import OutputService


## This class handles the collecting of matrices for further use
class Collector:

    __output_service: OutputService = OutputService()

    ##  Collects matrices and saves them to the specified path
    #
    #   @param amount of matrices to be created
    #   @param size of the matrices that will be created
    #   @param density of the matrices that will be created
    #   @param name of dataset under which matrices will be saved
    #   @param path where the matrices will be saved
    @staticmethod
    def collect(amount: int, size: int, name: str, path: str):
        collected_dataset = []
        observable: Observable = Observable()
        Collector.__output_service.print_stream("Collecting matrices %s/" + str(amount), observable)
        for i in range(0, amount):
            matrix = Generator.generate(size)
            collected_dataset.append(matrix)
            observable.next(str(i + 1))
        observable.complete()
        Saver.save(collected_dataset, name, path, False)
        Collector.__output_service.print_line("Finished collecting matrices. Saved at " + path + " under " + name)
        return collected_dataset

    ##  sets the static output service
    #
    #   use this to register your own output service at the start of the program
    #   this output service will be for called logs and results
    #   @param service OutputService that should be registered
    @staticmethod
    def set_output_service(service: OutputService):
        Collector.__output_service = service
