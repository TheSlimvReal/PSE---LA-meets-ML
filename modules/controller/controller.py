from modules.controller.command_parser import CommandParser
from modules.controller.commands.command import Command
from modules.controller.commands.quit_command import QuitCommand
from modules.exception.excpetions import IllegalArgumentException
from modules.view.cli_output_service import CLIOutputService
from modules.view.command_line_interface import CommandLineInterface


## Main entry point for program execution
#
#   it creates the view and executes the models
from modules.view.output_service import OutputService


class Controller:

    _view: CommandLineInterface
    _output_service: OutputService

    def __init__(self):
        self._view = CommandLineInterface()
        self._output_service = CLIOutputService(self._view)
        self._register_output_service()

    def start_interaction(self):
        finished: bool = False
        while not finished:
            try:
                command: Command = self._get_command()
                if isinstance(command, QuitCommand):
                    finished = True
                else:
                    command.execute()
            except IllegalArgumentException as e:
                self._output_service.print_error(str(e))
        self._output_service.print_line("Finished")

    def _get_command(self) -> Command:
        input_string: str = self._view.read_input("Which module do you want to execute?")
        command: Command = CommandParser.parse_input(input_string)
        return command



    def _register_output_service(self):
        pass
