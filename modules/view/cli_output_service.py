from modules.shared.matrix import Matrix
from modules.view.command_line_interface import CommandLineInterface
from modules.view.observable import Observable
from modules.view.output_service import OutputService
from modules.view.subscriber import Subscriber


##  This class communicates with the command line interface
class CLIOutputService(OutputService, Subscriber):

    view: CommandLineInterface

    message: str = ""

    def __init__(self, view: CommandLineInterface):
        self.view = view

    def print_line(self, line: str) -> None:
        self.view.print(line)

    def print_stream(self, message: str, observable: Observable):
        observable.add_subscriber(self)
        if "%s" not in message:
            message += " %s"
        self.message = message

    def print_error(self, error: str) -> None:
        super().print_error(error)

    def print_matrix(self, matrix: Matrix):
        super().print_matrix(matrix)

    def update(self, value: str) -> None:
        self.view.print_overriding(self.message % value)
