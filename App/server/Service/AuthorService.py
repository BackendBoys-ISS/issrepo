from server.repository.AuthorEntity import AuthorRepository
from server.repository.PaperEntity import PaperRepository
from server.repository.PaperKeywordEntity import PaperKeywordRepository
from server.repository.PaperTopicEntity import PaperTopicRepository
from server.repository.TopicEntity import TopicRepository
from server.repository.KeywordEntity import KeywordRepository
from server.repository.ContributionEntity import ContributionRepository
from server.repository.UserEntity import UserRepository


class AuthorService:
    def __init__(self):
        self.__userRepo = UserRepository()
        self.__authorRepo = AuthorRepository()
        self.__paperRepo = PaperRepository()
        self.__paperKeywordRepo = PaperKeywordRepository()
        self.__paperTopicRepo = PaperTopicRepository()
        self.__topicRepo = TopicRepository()
        self.__keywordRepo = KeywordRepository()
        self.__contributionRepo = ContributionRepository()
        self.__ids = [12, 23, 34, 45]

    def add_paper(self, authors, name, metadataa, document, topics, keywords):
        try:
            self.__paperRepo.add(self.__ids[1], name, metadataa, document)
            for author in authors:
                user = self.__userRepo.find_by_name(author)
                author_entity = self.__authorRepo.find_one_by_userID(user.userID)
                self.__contributionRepo.add(author_entity.authorID, self.__ids[1])

            for topic in topics:
                self.__topicRepo.add(self.__ids[3], topic)
                self.__paperTopicRepo.add(self.__ids[1], self.__ids[3])
                self.__ids[3] += 1

            for keyword in keywords:
                self.__keywordRepo.add(self.__ids[4], keyword)
                self.__paperKeywordRepo.add(self.__ids[1], self.__ids[4])
                self.__ids[4] += 1
            self.__ids[1] += 1
            return True
        except:
            return False

    def add_document(self, authorID, paperID, document):
        try:
            paper = self.__paperRepo.find_one(paperID)
            self.__paperRepo.update(paperID,paper.name,paper.metadataa,document)
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

    def getAllAuthorIDs(self):
        return[author.userID for author in self.__authorRepo.find_all()]

    def get_papers(self, authorID):
        paperIDs = self.__contributionRepo.find_by_author(authorID)
        papers = []
        for id in paperIDs:
            papers.append(self.__paperRepo.find_one(id))
        return papers

