from server.repository.AuthorEntity import AuthorRepository
from server.repository.PaperEntity import PaperRepository
from server.repository.PaperKeywordEntity import PaperKeywordRepository
from server.repository.PaperTopicEntity import PaperTopicRepository
from server.repository.TopicEntity import TopicRepository
from server.repository.KeywordEntity import KeywordRepository
from server.repository.ContributionEntity import ContributionRepository


class AuthorService:
    def __init__(self):
        self.__authorRepo = AuthorRepository()
        self.__paperRepo = PaperRepository()
        self.__paperKeywordRepo = PaperKeywordRepository()
        self.__paperTopicRepo = PaperTopicRepository()
        self.__topicRepo = TopicRepository()
        self.__keywordRepo = KeywordRepository()
        self.__contributionRepo = ContributionRepository()
        self.__ids = [12, 23, 34, 45]

    def add_paper(self, authorID, name, metadata, document):
        try:
            self.__paperRepo.add(self.__ids[1],name,metadata,document)
            self.__contributionRepo.add(authorID,self.__ids[2])
            self.__ids[1] += 1
            return True
        except:
            return False

    def add_document(self, authorID, paperID, document):
        try:
            paper = self.__paperRepo.find_one(paperID)
            self.__paperRepo.update(paperID,paper.name,paper.metadata,document)
        except:
            pass

    def add_topic(self, authorID, paperID, topic):
        try:
            self.__topicRepo.add(self.__ids[2],topic)
            self.__paperTopicRepo.add(paperID, self.__ids[2])
            self.__ids[2] += 1
            return True
        except:
            return False

    def add_keyword(self, authorID, paperID, keyword):
        try:
            self.__keywordRepo.add(self.__ids[3], keyword)
            self.__paperKeywordRepo.add(paperID, self.__ids[3])
            self.__ids[3] += 1
            return True
        except:
            return False

    def make_speaker(self, authorID):
        author = self.__authorRepo.find_one(authorID)
        self.__authorRepo.update(authorID,author.userID,author.affiliation,True)

    def is_speaker(self, authorID):
        author = self.__authorRepo.find_one(authorID)
        return author.isSpeaker


