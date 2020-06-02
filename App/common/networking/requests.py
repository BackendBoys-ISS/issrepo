import abc

from domain.Review import Review


class Request(abc.ABC):
    TIMEOUT = 10

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
        self.paper_1 = None  # set by server
        self.paper_2 = None  # set by server

    def get_reviewer_id(self):
        return self.reviewer_id


class LoginRequest(Request):

    def __init__(self, email, password):
        self.user = None  ###which enity is this, could be Author or PCMember
        self.email = email
        self.password = password
        self.result = 'not set'

    def __str__(self):
        return '' + self.email + ', ' + self.password + ', ' + self.result

    def get_loginEmail(self):
        return self.email

    def get_loginPassword(self):
        return self.password

    def get_loginResult(self):
        return self.result

    def set_loginResult(self, value: str):
        self.result = value


class CreateAccountRequest(Request):

    def __init__(self, fullName, email, password):
        self.fullName = fullName
        self.email = email
        self.password = password
        self.result = 'not set'

    def __str__(self):
        return '' + self.fullName + ', ' + self.email + ', ' + self.password + ', ' + self.result

    def get_createFullName(self):
        return self.fullName

    def get_createEmail(self):
        return self.email

    def get_cratePassword(self):
        return self.password

    def get_createAccountResult(self):
        return self.result

    def set_createAccountResult(self, value: str):
        self.result = value


class UploadAbstractRequest(Request):

    def __init__(self, paperName, kewords, topics, authors):
        self.paperName = paperName
        self.keywords = kewords[:]
        self.topics = topics[:]
        self.authors = authors[:]
        self.result = 'not done'

    def get_paperName(self):
        return self.paperName

    def get_keywords(self):
        return self.keywords

    def get_topics(self):
        return self.topics

    def get_authors(self):
        return self.authors

    def get_uploadAbstractResult(self):
        return self.result

    def set_uploadAbstractResult(self, value):
        self.result = value


class PaperListRequest(Request):    # PAPER LIST FROM BID
    def __init__(self):
        self.papers = []

    def get_papers(self):
        return self.papers

    def set_papers(self, papers):
        self.papers = papers[:]


class PaperListSubmitBidRequest(Request):
    def __init__(self, grade, paperId):
        self.grade = grade
        self.paperId = paperId

    def get_grade(self):
        return self.grade

    def get_paperId(self):
        return self.paperId

class ReviewerPapersRequest(Request):
    def __init__(self):
        self.papers = []

    def get_papers(self):
        return self.papers

    def set_papers(self, papers):
        self.papers = papers[:]

class ReviewerListRequest(Request):
    def __init__(self):
        self.reviewers = []

    def get_reviewers(self):
        return self.reviewers

    def set_reviewers(self, reviewers):
        self.reviewers = reviewers[:]

class ReviewRequest(Request):
    def __init__(self, reviewerId, paperId):
        self.reviewerId = reviewerId
        self.paperId = paperId
        self.review = None

    def get_reviewerId(self):
        return self.reviewerId

    def get_paperId(self):
        return self.paperId

    def get_review(self):
        return self.review

    def set_review(self, reviewResult: int, reviewEvaluation: str):
        self.review = Review(reviewResult, self.reviewerId, self.paperId, reviewEvaluation)
