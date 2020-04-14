import http.server
import logging
import queue
import random
import string
import threading
import time

from App.common.networking.request_handler import RequestHandler
from App.common.networking.request_sender import RequestSender
from App.common.networking.requests import Echo


DUMMY_SERVER_IP = '127.0.0.1'
DUMMY_SERVER_PORT = 1234


def get_dummy_request(text=None):
    if not text:
        text = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    return Echo(text)


def get_dummy_sender() -> RequestSender:
    dummy = RequestSender()
    dummy.SERVER_IP = DUMMY_SERVER_IP
    dummy.SERVER_PORT = DUMMY_SERVER_PORT
    return dummy


def get_dummy_server():
    return DummyServer()


class DummyServer:
    def __init__(self):
        self.logger = logging.getLogger("Dummy server")
        self.__queue = queue.Queue()
        RequestHandler.SERVER_REQUEST_QUEUE = self.__queue
        self.__http_server = http.server.HTTPServer((DUMMY_SERVER_IP, DUMMY_SERVER_PORT), RequestHandler)
        self.http_server_thread = threading.Thread(target=self.__http_server.serve_forever, args=())
        self.http_server_thread.start()
        print("HTTP SERVER STARTED")
        threading.Thread(target=self.process_requests, args=()).start()
        print("Processing thread started")

    def process_requests(self):
        while True:
            if self.__queue.empty():
                time.sleep(1)
                print("No requests to be processed; sleeping 1 sec")
            else:
                request = self.__queue.get()
                self.__consume(request)
                request.is_processed_event.set()

    def __consume(self, request):
        if isinstance(request, Echo):
            print(request.text)
