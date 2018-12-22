

##  Communicates with the command line
#
#   This class creates content for the command line and reads in the input
class CommandLineInterface:

    ##  Creates output to the command line
    #
    #   @param message the message that should be printed
    def create_output(self, message: str) -> None:
        print(message)

    ##  Prints a message and reads the user input
    #
    #   @param message the message that will be displayed first
    #   @return the string the user entered
    def read_input(self, message: str) -> str:
        input_line: str = input(message + "\n")
        return input_line
