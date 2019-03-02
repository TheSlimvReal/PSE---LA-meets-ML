

##  top level exception class
#
#   @extends Exception to be treated as a exception
class MyException(Exception):
    def __init__(self, message: str):
        self._type: str = None
        self.__message = message

    ##  get information about the error that occurred
    def get_info(self) -> str:
        return self.get_type() + ": " + self.__message

    ## abstract method to get type of the specific exception
    def get_type(self) -> str:
        pass


##  exception that should be thrown when the passed arguments are invalid
#
#   @extends MyException for generacl usage
class IllegalArgumentException(MyException):

    def get_type(self) -> str:
        return "IllegalArgumentException"


##  exception that should be thrown when the config file is incorrect
#
#   @extends MyException for general usage
class InvalidConfigException(MyException):

    def get_type(self) -> str:
        return "InvalidConfigException"


##  exception that should be thrown when input/output errors occur
#
#   @extends MyException for general usage
class IOException(MyException):

    def get_type(self) -> str:
        return "IOException"


##  exception that should be thrown when trying to access functions that are not supported on this operating system
#
#   @extends MyException for general usage
class InvalidOSException(MyException):

    def get_type(self) -> str:
        return "InvalidOSException"


##  exception that should be thrown in the body of each function in an interface
#
#   @extends MyException for general usage
class NotImplementedException(MyException):

    def get_type(self) -> str:
        return "NotImplementedException"