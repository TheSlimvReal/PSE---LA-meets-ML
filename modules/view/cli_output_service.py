from modules.exception.exceptions import MyException
from modules.view.command_line_interface import CommandLineInterface
from modules.view.observable import Observable
from modules.view.output_service import OutputService
from modules.view.subscriber import Subscriber
import numpy as np


##  This class communicates with the command line interface
class CLIOutputService(OutputService, Subscriber):

    def __init__(self, view: CommandLineInterface):
        self.__view: CommandLineInterface = view
        self.__message: str = ""

    def print_line(self, line: str) -> None:
        self.__view.print(line)

    def print_stream(self, message: str, observable: Observable):
        observable.add_subscriber(self)
        if "%s" not in message:
            message += " %s"
        self.__message = message

    def print_error(self, error: MyException) -> None:
        self.print_line(error.get_info())

    def update(self, value: str) -> None:
        self.__view.print_overriding(self.__message % value)

    def finished(self) -> None:
        self.print_line("")
