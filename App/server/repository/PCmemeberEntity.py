from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger, Boolean, String

db_string = "postgres://postgres:password@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class PCmember(base):
    __tablename__ = 'PCmembers'

    memberID = Column(BigInteger, primary_key=True)
    authorID = Column(BigInteger, ForeignKey("Authors.authorID"))
    website = Column(String)
    isChair = Column(Boolean)

    def __str__(self):
        return str(self.memberID) + " " + str(self.authorID) + " " + self.website + " " + str(self.isChair)


class PCmemberRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, memberID, authorID, website, isChair):
        pcmember = PCmember(memberID=memberID, authorID=authorID, website=website, isChair=isChair)
        self.__session.add(pcmember)
        self.__session.commit()

    def read(self):
        pcmemberList = []
        pcmembers = self.__session.query(PCmember)
        for pcmember in pcmembers:
            pcmemberList.append(pcmember)
        return pcmemberList

    def find_one(self, memberID):
        return self.__session.query(PCmember).filter(PCmember.memberID == memberID).one()

    def update(self, memberID, authorID, website, isChair):
        pcmember = self.find_one(memberID)
        pcmember.authorID = authorID
        pcmember.website = website
        pcmember.isChair = isChair
        self.__session.commit()

    def delete(self, memberID):
        pcmember = self.find_one(memberID)
        self.__session.delete(pcmember)
        self.__session.commit()
