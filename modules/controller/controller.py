from modules.controller.command_parser import CommandParser
from modules.controller.commands.command import Command
from modules.exception.excpetions import IllegalArgumentException
from modules.view.cli_output_service import CLIOutputService
from modules.view.command_line_interface import CommandLineInterface


## Main entry point for program execution
#
#   it creates the view and executes the models
from modules.view.output_service import OutputService


class Controller:

    view: CommandLineInterface
    output_service: OutputService

    def __init__(self):
        finished: bool = False
        view = CommandLineInterface()
        output_service = CLIOutputService(view)
        self._register_output_service()
        while not finished:
            command: Command = self._get_command()
            if isinstance(command, Command):
                finished = True
            else:
                command.execute()

        output_service.print_line("Finished")

    def _get_command(self) -> Command:
        input_string: str = self.view.read_input("Which module do you want to execute?")
        command: Command
        try:
            command = CommandParser.parse_input(input_string)
        except IllegalArgumentException as e:
            self.output_service.print_error(str(e))
        return command


    def _register_output_service(self):
        pass

