from sqlalchemy import create_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger

db_string = "postgres://postgres:password@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Section(base):
    __tablename__ = 'Sections'

    sectionID = Column(BigInteger, primary_key=True)
    speakerID = Column(BigInteger, ForeignKey("Authors.authorID"))
    conferenceID = Column(BigInteger, ForeignKey("Conferences.conferenceID"))
    supervisorID = Column(BigInteger, ForeignKey("PCmembers.memberID"))
    roomID = Column(BigInteger, ForeignKey("Rooms.roomID"))
    programID = Column(BigInteger, ForeignKey("Programs.programID"))

    def __str__(self):
        return str(self.sectionID) + " " + str(self.speakerID) + " " + str(self.conferenceID) + " " +\
               str(self.supervisorID) + " " + str(self.roomID) + " " +str(self.programID)


class SectionRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, sectionID, speakerID, conferenceID, supervisorID, roomID, programID):
        section = Section(sectionID=sectionID, speakerID=speakerID, conferenceID=conferenceID, supervisorID=supervisorID, roomID=roomID, programID=programID)
        self.__session.add(section)
        self.__session.commit()

    def read(self):
        sectionList = []
        sections = self.__session.query(Section)
        for section in sections:
            sectionList.append(section)
        return sectionList

    def find_one(self, sectionID):
        return self.__session.query(Section).filter(Section.sectionID == sectionID).one()

    def update(self, sectionID, speakerID, conferenceID, supervisorID, roomID, programID):
        section = self.find_one(sectionID)
        section.speakerID = speakerID
        section.conferenceID = conferenceID
        section.supervisorID = supervisorID
        section.roomID = roomID
        section.programID = programID
        self.__session.commit()

    def delete(self, sectionID):
        section = self.find_one(sectionID)
        self.__session.delete(section)
        self.__session.commit()
