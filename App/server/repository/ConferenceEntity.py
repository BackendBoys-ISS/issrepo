from sqlalchemy import create_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger, Date

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Conference(base):
    __tablename__ = 'Conferences'

    conferenceID = Column(BigInteger, primary_key=True)
    conferenceName = Column(String)
    startingDate = Column(Date)
    endingDate = Column(Date)
    abstractDeadline = Column(Date)
    proposalDeadline = Column(Date)
    biddingDeadline = Column(Date)
    programID = Column(BigInteger, ForeignKey("Programs.programID"))

    def __str__(self):
        return str(self.conferenceID) + " " + self.conferenceName + " " + str(self.startingDate) + \
               " " + str(self.endingDate) + " " + str(self.abstractDeadline) + " " + str(self.proposalDeadline) + \
               " " + str(self.biddingDeadline) + " " + str(self.programID)


class ConferenceRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, conferenceID, conferenceName, startingDate, endingDate, abstractDeadline, proposalDeadline, biddingDeadline, programID):
        conference = Conference(conferenceID=conferenceID, conferenceName=conferenceName, startingDate=startingDate,
                                endingDate=endingDate, abstractDeadline=abstractDeadline,
                                proposalDeadline=proposalDeadline, biddingDeadline=biddingDeadline, programID=programID
                                )
        self.__session.add(conference)
        self.__session.commit()

    def read(self):
        conferenceList = []
        conferences = self.__session.query(Conference)
        for conference in conferences:
            conferenceList.append(conference)
        return conferenceList

    def find_one(self, conferenceID):
        return self.__session.query(Conference).filter(Conference.conferenceID == conferenceID).one()

    def update(self, conferenceID, conferenceName, startingDate, endingDate, abstractDeadline, proposalDeadline, biddingDeadline, programID):
        conference = self.find_one(conferenceID)
        conference.conferenceName = conferenceName
        conference.startingDate = startingDate
        conference.endingDate = endingDate
        conference.abstractDeadline = abstractDeadline
        conference.proposalDeadline = proposalDeadline
        conference.biddingDeadline = biddingDeadline
        conference.programID = programID
        self.__session.commit()

    def delete(self, conferenceID):
        conference = self.find_one(conferenceID)
        self.__session.delete(conference)
        self.__session.commit()


