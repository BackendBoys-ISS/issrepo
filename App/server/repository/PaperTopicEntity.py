from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class PaperTopic(base):
    __tablename__ = 'PaperTopics'

    paperID = Column(BigInteger, ForeignKey("Papers.paperID"), primary_key=True)
    topicID = Column(BigInteger, ForeignKey("Topics.topicID"), primary_key=True)

    def __str__(self):
        return str(self.paperID) + " " + str(self.topicID)


class PaperTopicRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, paperID, topicID):
        papertopic = PaperTopic(paperID=paperID, topicID=topicID)
        self.__session.add(papertopic)
        self.__session.commit()

    def read(self):
        papertopicList = []
        papertopics = self.__session.query(PaperTopic)
        for papertopic in papertopics:
            papertopicList.append(papertopic)
        return papertopicList

    def find_one(self, paperID, topicID):
        return self.__session.query(PaperTopic).filter(PaperTopic.paperID == paperID).filter(PaperTopic.topicID == topicID).one()

    def update(self, paperID, topicID):
        pass

    def delete(self, paperID, topicID):
        papertopic = self.find_one(paperID, topicID)
        self.__session.delete(papertopic)
        self.__session.commit()
