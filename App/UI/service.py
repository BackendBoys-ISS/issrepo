from client.client import Client
from common.networking.request_sender import RequestSender
from common.networking.requests import LoginRequest


class Service:
    def __init__(self):
        self.rqSender = Client()
        pass

    def loginCheck(self, email: str, password: str):
        result = self.rqSender.sendLoginRequest(email, password)
        print(result.get_loginResult())
        return result.get_loginResult()

    def createAccountCheck(self, fullName: str, email: str, password: str):
        result = self.rqSender.sendCreateAccountRq(fullName, email, password)
        print(result.get_createAccountResult())
        return result.get_createAccountResult()

    def uploadAbstractCheck(self, paperName: str, keywords, topics, authors):
        result = self.rqSender.sendUploadAbstractRequest(paperName, keywords, topics, authors)
        return result.get_uploadAbstractResult()

    def paperListCheck(self):
        result = self.rqSender.sendPaperListRequest()
        return result.get_papers()

    def paperListSubmitBidCheck(self, grade, paperId):
        result = self.rqSender.sendPaperListSubmitBidRequest(grade, paperId)
        return result

    def reviewerPapersCheck(self):
        result = self.rqSender.sendReviewerPapersRequest()
        return result.get_papers()

    def reviewersListCheck(self):
        result = self.rqSender.sendReviewersListRequest()
        return result.get_reviewers()

    def reviewCheck(self, reviewerId, paperId):
        result = self.rqSender.sendReviewRequest(reviewerId, paperId)
        return result