import sys


##  Communicates with the command line
#
#   This class creates content for the command line and reads in the input
class CommandLineInterface:

    ##  Creates output to the command line
    #
    #   @param message the message that should be printed
    def print_to_view(self, message: str) -> None:
        print(message)

    ##  Prints a message and reads the user input
    #
    #   @param message the message that will be displayed first
    #   @return the string the user entered
    def read_input(self, message: str) -> str:
        input_line: str = input(message)
        return input_line

    def print_overriding(self, line: str) -> None:
        sys.stdout.write(line)
        sys.stdout.flush()
