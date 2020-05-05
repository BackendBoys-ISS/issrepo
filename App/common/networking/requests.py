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

class ReviewerShit(Request):

    def __init__(self, reviewer_id):
        self.reviewer_id = reviewer_id
        # paper_1 and paper_2 can be objects as long as the client has access to them
        self.paper_1 = None # set by server
        self.paper_2 = None # set by server

    def get_reviewer_id(self):
        return self.reviewer_id