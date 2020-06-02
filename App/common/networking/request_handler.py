import http.server
import logging
import pickle
import threading
import time
from common.networking.requests import Request


class RequestHandler(http.server.BaseHTTPRequestHandler):
    SERVER_REQUEST_QUEUE = None  # this is set when the server initializes
    HTTP_STATUS_BAD_REQUEST = 400
    HTTP_STATUS_OK = 200
    HTTP_STATUS_INTERNAL_SERVER_ERROR = 500

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('mainlogger.RequestHandler.{}'.format(client_address))
        spawn_time = time.time()
        try:
            http.server.BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        except Exception as ex:
            self.logger.exception(ex)
            self.logger.error('EXC http.server.BaseHTTPRequestHandler(%s, %s, %s) in %6.4f seconds' %
                              (request, client_address, server, time.time() - spawn_time))
            raise

    def do_POST(self):
        """
        Entry point for all incoming requests
        Puts a request in SERVER's queue. awaits its processing and sends back the processed request obj
        """
        request_timeout = float(self.headers.get('Request-Timeout', 10))
        request = self.__get_request()
        self.SERVER_REQUEST_QUEUE.put(request)
        if not request.is_processed_event.wait(request_timeout):
            request.exception = Exception("Request timeout exceeded {} for {}".format(request_timeout, request))

        self.__send_processed_response(request)

    def __get_request(self) -> Request:
        raw_bytes = self.rfile.read(int(self.headers['Content-Length']))
        request_obj: Request = pickle.loads(raw_bytes)
        request_obj.is_processed_event = threading.Event()
        return request_obj

    def __send_processed_response(self, response: Request):
        response.is_processed_event = None  # removing the event because it can't be pickled
        self.send_response(self.HTTP_STATUS_OK)
        self.send_header('Content-type', 'text/octet-stream')
        raw_response = pickle.dumps(response)
        self.end_headers()
        self.wfile.write(raw_response)
