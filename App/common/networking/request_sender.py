import pickle
import urllib.request

from App.common.networking.requests import Request


class RequestSender:
    SERVER_IP = None
    SERVER_PORT = None

    def send_request_to_server(self, request: Request):
        if not self.SERVER_IP or not self.SERVER_PORT:
            raise ValueError("Server ip and port values were not set")
        print("will send {} to {}:{}".format(request, self.SERVER_IP, self.SERVER_PORT))
        return self.__send_request(request)

    def __send_request(self, request: Request):
        target_url = "http://{}:{}".format(self.SERVER_IP, self.SERVER_PORT)
        headers = {
            'Content-Type': 'application/octet-stream',
            'Request-Timeout': str(request.TIMEOUT),
        }
        request_bytes = pickle.dumps(request)
        try:
            resource = urllib.request.urlopen(urllib.request.Request(target_url, request_bytes, headers),
                                              timeout=request.TIMEOUT)
            response: Request = pickle.loads(resource.read())
        except Exception as e:
            response = request
            response.exception = e
        return response
