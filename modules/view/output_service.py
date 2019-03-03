from modules.exception.exceptions import MyException
from modules.view.observable import Observable


##  Empty class for services that can be registered to a module
#
#   This class offers no functionality but is a placeholder for any implementations
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
