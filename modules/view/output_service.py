from modules.exception.excpetions import MyException
import numpy as np
from modules.view.observable import Observable


##  Interface for services that can be registered to a module
#
#   Use this as default and any other OutputService can be registered during runtime
class OutputService:

    ##  Prints a line to the view
    #
    #   @param line the line that should be printed
    def print_line(self, line: str) -> None:
        pass

    ##  Prints an self overriding string
    #
    #   @param message the line that will stay the same
    #   @param observable where the updates of the values can be retrieved
    def print_stream(self, message: str, observable: Observable) -> None:
        pass

    ##  Prints an exception to the view
    #
    #   @param error the error holding a message
    def print_error(self, error: MyException) -> None:
        pass

    ##  Prints a matrix to the view
    #
    #   @param matrix that will be displayed
    def print_matrix(self, matrix: np.ndarray) -> None:
        pass
