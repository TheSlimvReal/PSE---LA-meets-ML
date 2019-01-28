from modules.controller.command_parser import CommandParser
from modules.controller.commands.command import Command
from modules.controller.commands.help_command import HelpCommand
from modules.controller.commands.key import Key
from modules.controller.commands.quit_command import QuitCommand
from modules.exception.excpetions import IllegalArgumentException
from modules.model.classification_module.classification_module import Classifier
from modules.model.collector_module.collector import Collector
from modules.model.labeling_module.labeling_module import LabelingModule
from modules.model.training_module.training_module import TrainingModule
from modules.view.cli_output_service import CLIOutputService
from modules.view.command_line_interface import CommandLineInterface
from modules.view.output_service import OutputService


## Main entry point for program execution
#
#   it creates the view and executes the models
class Controller:

    ##  Constructor sets up all the classes for the MVC
    def __init__(self):
        self.__view: CommandLineInterface = CommandLineInterface()
        self.__output_service: OutputService = CLIOutputService(self.__view)
        self.__register_output_service()

    ##  Starts user interaction with the command line
    def start_interaction(self):
        finished: bool = False
        while not finished:
            command: Command = self.__get_command()
            if isinstance(command, QuitCommand):
                finished = True
            elif isinstance(command, HelpCommand):
                self.__print_main_help_information(command)
            elif Key.HELP in command.arguments:
                self.__print_help_information(command)
            else:
                command.execute()
        self.__output_service.print_line("Finished")

    def __get_command(self) -> Command:
        input_string = self.__view.read_input("Which module do you want to execute?")
        try:
            command = CommandParser.parse_input(input_string)
        except IllegalArgumentException as e:
            self.__output_service.print_error(e)
            command = self.__get_command()
        return command

    def __register_output_service(self):
        Collector.set_output_service(self.__output_service)
        LabelingModule.set_output_service(self.__output_service)
        TrainingModule.set_output_service(self.__output_service)
        Classifier.set_output_service(self.__output_service)

    def __print_help_information(self, command: Command):
        self.__view.print("These are the possible Tags for the " + command.module_name.value + "-command:")
        for info in command.help_arguments:
            self.__view.print(info)

    def __print_main_help_information(self, command):
        self.__view.print("These are the possible interactions:")
        for command in CommandParser.get_valid_commands():
            self.__view.print(command)
        self.__view.print("for more information type in the command and -h or --help.")
