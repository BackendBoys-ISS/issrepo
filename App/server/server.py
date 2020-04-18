import http.server
import queue
import socket
import threading
import time

from common.networking.request_handler import RequestHandler
import traceback

import common.networking.requests as req


class Server:
    REAL_PORT = DUMMY_PORT = 2307
    REAL_IP = None
    DUMMY_IP = '127.0.0.1'
    REQUEST_PROCESSORS_NUMBER = 4

    def __init__(self, use_dummy=False):
        self.__request_queue = queue.Queue()
        try:
            self.__init_http_server(use_dummy)
            self.__init_request_processors()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            raise AttributeError("Errors in init; exiting server")

    def __init_http_server(self, use_dummy=True):
        if use_dummy:
            address_tuple = (self.DUMMY_IP, self.DUMMY_PORT)
        else:
            host_name = socket.gethostname()
            self.REAL_IP = socket.gethostbyname(host_name)
            address_tuple = (self.REAL_IP, self.REAL_PORT)

        RequestHandler.SERVER_REQUEST_QUEUE = self.__request_queue
        self.__http_server = http.server.HTTPServer(address_tuple, RequestHandler)
        # http server needs to run on a separate thread; otherwise it blocks the current thread
        self.__http_server = threading.Thread(target=self.__http_server.serve_forever, args=())
        self.__http_server.start()
        print("HTTP SERVER STARTED")

    def __init_request_processors(self):
        self.__request_processors = list()
        for _ in range(self.REQUEST_PROCESSORS_NUMBER):
            self.__request_processors.append(threading.Thread(target=self.__process_request, args=()))
        for processing_thread in self.__request_processors:
            processing_thread.start()
        print("{} REQUEST PROCESSORS STARTED".format(self.REQUEST_PROCESSORS_NUMBER))

    def __process_request(self):
        while True:
            if self.__request_queue.empty():
                time.sleep(1)
            else:
                request_obj = self.__request_queue.get()
                self.__execute(request_obj)
                request_obj.is_processed_event.set()

    def __execute(self, request_obj: req.Request):
        # switch case for use cases
        if isinstance(request_obj, req.Echo):
            self.__echo(request_obj)

    def __echo(self, request_obj): # used for testing
        print(request_obj.text)
        request_obj.response_from_server = 'server response'



