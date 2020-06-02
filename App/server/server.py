import http.server
import queue
import socket
import threading
import time

from common.networking.request_handler import RequestHandler
import traceback

import common.networking.requests as req
from server.Service.AuthorService import AuthorService
from server.Service.UserService import UserService


class Server:
    REAL_PORT = DUMMY_PORT = 2307
    REAL_IP = "127.0.0.1"
    DUMMY_IP = '127.0.0.1'
    REQUEST_PROCESSORS_NUMBER = 4
    def __init__(self, use_dummy=False):
        self.__request_queue = queue.Queue()
        try:
            self.__init_http_server(use_dummy)
            self.__init_request_processors()
            self.__user_service = UserService()
            self.__author_service = AuthorService()

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
        print(address_tuple)

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
        print("switch?")
        if isinstance(request_obj, req.Echo):
            self.__echo(request_obj)
        elif isinstance(request_obj, req.LoginRequest):
            self.__log_in(request_obj)
        elif isinstance(request_obj, req.CreateAccountRequest):
            self.__create_account(request_obj)
        elif isinstance(request_obj, req.UploadAbstractRequest):
            self.__upload_abstract(request_obj)
        elif isinstance(request_obj, req.PaperListRequest):
            self.__handlePaperListReq(request_obj)
        elif isinstance(request_obj, req.PaperListSubmitBidRequest):
            self.__paperListSubmitBid(request_obj)
        elif isinstance(request_obj, req.ReviewerPapersRequest):
            self.__reviewerPapersRequest(request_obj)
        elif isinstance(request_obj, req.ReviewerListRequest):
            self.__reviewerListRequest(request_obj)
        elif isinstance(request_obj, req.ReviewRequest):
            self.__reviewRequest(request_obj)



    # exemplu pentru cum trebuie sa se comporte metodele server-ului
    # 1. ia datele primate de la client(din obiectul de tip request)
    # 2. le paseaza la o metoda care face business logic cu ele
    # 3. seteaza un rezultat pe obiectul de tip request
    # e bine sa fie pentru ca e usor de testat atat izolat cat si use-case intreg
    # pentru testare izolate puteti testat doar self__do_work()
    # def example_method(self, request_obj):
    #     x, y, z = request_obj.x, request_obj.y, request_obj.z
    #     data_wanted_by_client = self.__do_work(x, y, z)
    #     request_obj.set_response(data_wanted_by_client)


    def __echo(self, request_obj): # used for testing
        print(request_obj.text)
        request_obj.response_from_server = 'server response'

    def __log_in(self, request_obj):
        print("ok?")
        request_obj.result = self.__user_service.login(request_obj.get_loginEmail(), request_obj.get_loginPassword())

    def __create_account(self, request_obj):
        request_obj.result = self.__user_service.create_account(request_obj.get_createEmail(), request_obj.get_cratePassword(),
                                                                request_obj.get_createFullName(), request_obj.get_createFullName())

    def __upload_abstract(self, request_obj):
        print(request_obj.get_keywords(), request_obj.get_authors(), request_obj.get_topics())
        request_obj.result = self.__author_service.add_paper(request_obj.get_authors(), request_obj.get_paperName(), "",
                                                             "", request_obj.get_topics(), request_obj.get_keywords())

    def __handlePaperListReq(self, request_obj):
        papers = []
        for authorID in self.__author_service.getAllAuthorIDs():
            for paper in self.__author_service.get_papers(authorID):
                papers.append(paper)
        request_obj.set_papers(papers)

    def __paperListSubmitBid(self, request_obj):
        pass


    def __reviewerPapersRequest(self, request_obj):
        pass

    def __reviewerListRequest(self, request_obj):
        pass

    def __reviewRequest(self, request_obj):
        pass


if __name__ == '__main__':
    Server(use_dummy=False)