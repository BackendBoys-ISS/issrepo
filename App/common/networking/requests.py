import abc


class Request(abc.ABC):
    TIMEOUT = None

    def __init__(self):
        self.is_processed_event = None
        self.exception = None

    def was_successful(self):
        return self.exception is None

    def get_exception(self) -> Exception:
        return self.exception


class Echo(Request):
    TIMEOUT = 5

    def __init__(self, text):
        super().__init__()
        self.text = text

    def __str__(self):
        return 'Echo: {}'.format(self.text)
