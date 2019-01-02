class MyException(Exception):
    def __init__(self, message: str):
        self._type: str = None
        self.__message = message

    def get_info(self) -> str:
        return self.get_type() + ": " + self.__message

    def get_type(self) -> str:
        pass


class IllegalArgumentException(MyException):

    def get_type(self) -> str:
        return "IllegalArgumentException"


class InvalidConfigException(MyException):

    def get_type(self) -> str:
        return "InvalidConfigException"


class IOException(MyException):

    def get_type(self) -> str:
        return "IOException"


class InvalidOSException(MyException):

    def get_type(self) -> str:
        return "InvalidOSException"
