from common.networking.request_sender import RequestSender
from common.networking.requests import *
from domain.Author import Author
from domain.Keyword import Keyword
from domain.PCMember import PCMember
from domain.Paper import Paper
from domain.Topic import Topic
from domain.User import User


class Client:
    DUMMY_SERVER_IP = '127.0.0.1'
    DUMMY_SERVER_PORT = REAL_SERVER_PORT = 2307
    REAL_SERVER_IP = "192.168.56.1" # hardcoded or read from .cfg file

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
        #print("Server response to our echo is {}".format(response.response_from_server))

    def sendLoginRequest(self, email, password):
        response = self.send_request(LoginRequest(email, password))
        return response

    def sendCreateAccountRq(self, fullName, email, password):
        response = self.send_request(CreateAccountRequest(fullName, email, password))
        return response

    def sendUploadAbstractRequest(self, paperName, keywords, topics, authors):
        response = self.send_request(UploadAbstractRequest(paperName, keywords, topics, authors))
        return response

    def sendPaperListRequest(self):
        response = self.send_request(PaperListRequest())
        response.set_papers([Paper(1, 'paper1', 'metadata', [str(Keyword(1, 'key1')), str(Keyword(2, 'key2'))],
                                   [str(Topic(1, 'topic1'))], 'document.smthg')])

        return response

    def sendPaperListSubmitBidRequest(self, grade, paperId):
        response = self.send_request(PaperListSubmitBidRequest(grade, paperId))
        return response

    def sendReviewerPapersRequest(self):
        response = self.send_request(ReviewerPapersRequest())
        response.set_papers([Paper(1, 'paper1', 'metadata', [str(Keyword(1, 'key1')), str(Keyword(2, 'key2'))],
                                   [str(Topic(1, 'topic1'))], 'document.smthg')])
        return response

    def sendReviewersListRequest(self):
        response = self.send_request(ReviewerListRequest())
        response.set_reviewers([PCMember(1, 'website', False, Author(1, None, False, [Paper(1, 'paper1', 'metadata',
                                                        [str(Keyword(1, 'key1')), str(Keyword(2, 'key2'))],
                                                        [str(Topic(1, 'topic1'))], 'document.smthg')], User(1, 'email',
                                                            'password', 'name', 'username')))])
        return response

    def sendReviewRequest(self, reviewerId, paperId):
        response = self.send_request(ReviewRequest(reviewerId, paperId))
        response.set_review(3, 'very good')
        return response

    # methods should:
    # have as params data from the UI
    # send a specific request using those params
    # do something with the response/ data from response
    # example method: think about echo() method above and image it returns something to be printed on ui
