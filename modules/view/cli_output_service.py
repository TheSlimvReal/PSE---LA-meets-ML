from modules.shared.matrix import Matrix
from modules.view.command_line_interface import CommandLineInterface
from modules.view.observable import Observable
from modules.view.output_service import OutputService
from modules.view.subscriber import Subscriber


##  This class communicates with the command line interface
class CLIOutputService(OutputService, Subscriber):

    view: CommandLineInterface

    def __init__(self, view: CommandLineInterface):
        self.view = view

    def print_line(self, line: str) -> None:
        super().print_line(line)

    def print_overriding(self, message: str, observable: Observable):
        super().print_overriding(message, observable)

    def print_error(self, error: str) -> None:
        super().print_error(error)

    def print_matrix(self, matrix: Matrix):
        super().print_matrix(matrix)

    def update(self, value: str) -> None:
        super().update(value)
