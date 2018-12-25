class MyException(Exception):

    _message: str

    def __init__(self, message: str):
        self._message = message

    def get_info(self) -> str:
        return self._message


class IllegalArgumentException(MyException):
    pass


class InvalidConfigException(MyException):
    pass


class IOException(MyException):
    pass


class InvalidOSException(MyException):
    pass
