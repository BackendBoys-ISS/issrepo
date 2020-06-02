from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class PaperKeyword(base):
    __tablename__ = 'PaperKeywords'

    paperID = Column(BigInteger, ForeignKey("Papers.paperID"), primary_key=True)
    keywordID = Column(BigInteger, ForeignKey("Keywords.keywordID"), primary_key=True)

    def __str__(self):
        return str(self.paperID) + " " + str(self.keywordID)


class PaperKeywordRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, paperID, keywordID):
        paperkeyword = PaperKeyword(paperID=paperID, keywordID=keywordID)
        self.__session.add(paperkeyword)
        self.__session.commit()

    def read(self):
        paperkeywordList = []
        paperkeywords = self.__session.query(PaperKeyword)
        for paperkeyword in paperkeywords:
            paperkeywordList.append(paperkeyword)
        return paperkeywordList

    def find_one(self, paperID, keywordID):
        return self.__session.query(PaperKeyword).filter(PaperKeyword.paperID == paperID).filter(PaperKeyword.keywordID == keywordID).one()

    def update(self, paperID, keywordID):
        pass

    def delete(self, paperID, keywordID):
        paperkeyword = self.find_one(paperID, keywordID)
        self.__session.delete(paperkeyword)
        self.__session.commit()
