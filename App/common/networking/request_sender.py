import pickle
import urllib.request

from App.common.networking.requests import Request


class RequestSender:
    def __init__(self, server_ip, server_port):
        self.__server_ip = server_ip
        self.__server_port = server_port

    def send_request_to_server(self, request: Request):
        if not self.__server_ip or not self.__server_port:
            raise ValueError("Server ip and port values were not set")
        print("will send {} to {}:{}".format(request, self.__server_ip, self.__server_port))
        return self.__send_request(request)

    def __send_request(self, request: Request):
        target_url = "http://{}:{}".format(self.__server_ip, self.__server_port)
        headers = {
            'Content-Type': 'application/octet-stream',
            'Request-Timeout': str(request.TIMEOUT),
        }
        request_bytes = pickle.dumps(request)
        try:
            resource = urllib.request.urlopen(urllib.request.Request(target_url, request_bytes, headers),
                                              timeout=request.TIMEOUT)
            response = pickle.loads(resource.read())
        except Exception as e:
            response = request
            response.exception = e
        return response
