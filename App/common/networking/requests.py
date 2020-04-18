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
    TIMEOUT = 1000

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.response_from_server = None

    def __str__(self):
        return 'Echo: {}'.format(self.text)
