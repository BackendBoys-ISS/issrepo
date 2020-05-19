from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger

db_string = "postgres://postgres:password@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Topic(base):
    __tablename__ = 'Users'

    topicID = Column(BigInteger, primary_key=True)
    topic = Column(String)

    def __str__(self):
        return str(self.topicID) + " " + self.topic



class TopicRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, topicID, topic):
        topic = Topic(topicID=topicID, topic=topic)
        self.__session.add(topic)
        self.__session.commit()

    def read(self):
        topicList = []
        topics = self.__session.query(Topic)
        for topic in topics:
            topicList.append(topic)
        return topicList

    def find_one(self, topicID):
        return self.__session.query(Topic).filter(Topic.topicID==topicID).one()

    def update(self, topicID, topic):
        topicc = self.find_one(topicID)
        topicc.email = topic
        self.__session.commit()

    def delete(self, topicID):
        topicc = self.find_one(topicID)
        self.__session.delete(topicc)
        self.__session.commit()