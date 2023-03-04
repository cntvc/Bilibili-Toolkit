class BilibiliException(Exception):
    def __init__(self, msg: str, *args) -> None:
        self.msg = msg.format(*args)
        super().__init__(self.msg)


class FileNotFoundError(BilibiliException):
    pass


class ConfigValueError(BilibiliException):
    pass
