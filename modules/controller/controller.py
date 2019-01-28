from modules.controller.command_parser import CommandParser
from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.controller.commands.quit_command import QuitCommand
from modules.exception.excpetions import IllegalArgumentException
from modules.view.cli_output_service import CLIOutputService
from modules.view.command_line_interface import CommandLineInterface


## Main entry point for program execution
#
#   it creates the view and executes the models
from modules.view.output_service import OutputService


class Controller:

    def __init__(self):
        self.__view: CommandLineInterface = CommandLineInterface()
        self.__output_service: OutputService = CLIOutputService(self.__view)
        self.__register_output_service()

    def start_interaction(self):
        finished: bool = False
        while not finished:
            command: Command = self._get_command()
            if isinstance(command, QuitCommand):
                finished = True
            elif Key.HELP in command.arguments:

            else:
                command.execute()
        self.__output_service.print_line("Finished")

    def _get_command(self) -> Command:
        input_string = self.__view.read_input("Which module do you want to execute?")
        try:
            command = CommandParser.parse_input(input_string)
        except IllegalArgumentException as e:
            self.__output_service.print_error(e)
            command = self._get_command()
        return command

    def __register_output_service(self):
        pass

    def __print_help_information(self, command: Command):
        self.__view.print("These are the possible Tags ")
