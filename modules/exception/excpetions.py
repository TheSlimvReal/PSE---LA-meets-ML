class IllegalArgumentException(Exception):

    message: str

    def __init__(self, message: str):
        self.message = message


class InvalidConfigException(Exception):
    pass


class IOException(Exception):
    pass


class InvalidOSException(Exception):
    pass
