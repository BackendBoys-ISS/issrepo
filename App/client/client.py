from common.networking.request_sender import RequestSender
from common.networking.requests import Request, Echo


class Client:
    DUMMY_SERVER_IP = '127.0.0.1'
    DUMMY_SERVER_PORT = REAL_SERVER_PORT = 2307
    REAL_SERVER_IP = None # hardcoded or read from .cfg file

    def __init__(self, use_dummy=False):
        self.__init_request_sender(use_dummy)

    def __init_request_sender(self, use_dummy=True):
        if use_dummy:
            self.__request_sender = RequestSender(self.DUMMY_SERVER_IP,
                                                  self.DUMMY_SERVER_PORT)
        else:
            self.__request_sender = RequestSender(self.REAL_SERVER_IP,
                                                  self.REAL_SERVER_PORT)

    def send_request(self, request_obj: Request) -> Request:
        return self.__request_sender.send_request_to_server(request_obj)

    def echo(self, text):
        response = self.send_request(Echo(text))
        print("Server response to our echo is {}".format(response.response_from_server))

    # methods should:
        # have as params data from the UI
        # send a specific request using those params
        # do something with the response/ data from response