from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Keyword(base):
    __tablename__ = 'Keywords'

    keywordID = Column(BigInteger, primary_key=True)
    keyword = Column(String)

    def __str__(self):
        return str(self.keywordID) + " " + self.keyword


class KeywordRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, keywordID, keyword):
        keywordd = Keyword(keywordID=keywordID, keyword=keyword)
        self.__session.add(keywordd)
        self.__session.commit()

    def read(self):
        keywordList = []
        keywords = self.__session.query(Keyword)
        for keyword in keywords:
            keywordList.append(keyword)
        return keywordList

    def find_one(self, keywordID):
        return self.__session.query(Keyword).filter(Keyword.keywordID == keywordID).one()

    def update(self, keywordID, keyword):
        keywordd = self.find_one(keywordID)
        keywordd.keyword = keyword
        self.__session.commit()

    def delete(self, keywordID):
        keywordd = self.find_one(keywordID)
        self.__session.delete(keywordd)
        self.__session.commit()
