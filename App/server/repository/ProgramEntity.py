from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger, Integer, Date, Time

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Program(base):
    __tablename__ = 'Programs'

    programID = Column(BigInteger, primary_key=True)
    calendarDate = Column(Date)
    hoursInterval = Column(Time)

    def __str__(self):
        return str(self.programID) + " " + str(self.calendarDate) + " " + str(self.hoursInterval)


class ProgramRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, programID, calendarDate, hoursInterval):
        program = Program(programID=programID, calendarDate=calendarDate, hoursInterval=hoursInterval)
        self.__session.add(program)
        self.__session.commit()

    def read(self):
        programList = []
        programs = self.__session.query(Program)
        for program in programs:
            programList.append(program)
        return programList

    def find_one(self, programID):
        return self.__session.query(Program).filter(Program.programID == programID).one()

    def update(self, programID, calendarDate, hoursInterval):
        program = self.find_one(programID)
        program.calendarDate = calendarDate
        program.hoursInterval = hoursInterval
        self.__session.commit()

    def delete(self, programID):
        program = self.find_one(programID)
        self.__session.delete(program)
        self.__session.commit()
