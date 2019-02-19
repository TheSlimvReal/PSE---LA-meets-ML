from modules.exception.exceptions import MyException
from modules.view.command_line_interface import CommandLineInterface
from modules.view.observable import Observable
from modules.view.output_service import OutputService
from modules.view.subscriber import Subscriber


##  This class communicates with the command line interface
#
#   @extends OutputService so it can be passed to a module
#   @extends Subscriber so it can be subscribe itself on an observer
class CLIOutputService(OutputService, Subscriber):

    def __init__(self, view: CommandLineInterface):
        self.__view: CommandLineInterface = view
        self.__message: str = ""

    ##  prints a string on the view
    #
    #   @param line string to be printed
    def print_line(self, line: str) -> None:
        self.__view.print(line)

    ##  setup function to print streams
    #
    #   @param message that will stay the same during the printing process, add a %s to define where the new
    #                   values should be inserted. If not set, the values will be appended
    #   @param observable which is used to get updates on new values
    def print_stream(self, message: str, observable: Observable):
        observable.add_subscriber(self)
        if "%s" not in message:
            message += " %s"
        self.__message = message

    ##  prints a error message to the view
    #
    #   @param error the exception for which a message should be printed
    def print_error(self, error: MyException) -> None:
        self.print_line(error.get_info())

    ##  updates the overriding string
    #
    #   @param value that is new
    def update(self, value: str) -> None:
        self.__view.print_overriding(self.__message % value)

    ##  finishes the overriding stream process
    def finished(self) -> None:
        self.print_line("")
