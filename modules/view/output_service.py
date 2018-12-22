from modules.shared.matrix import Matrix
from modules.view.observable import Observable


##  Interface for services that can be registered to a module
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
    def print_overriding(self, message: str, observable: Observable):
        pass

    ##  Prints an exception to the view
    #
    #   @param exception the string with the exception message
    def print_error(self, error: str) -> None:
        pass

    ##  Prints a matrix to the view
    #
    #   @param matrix the matrix that will be displayed
    def print_matrix(self, matrix: Matrix):
        pass
