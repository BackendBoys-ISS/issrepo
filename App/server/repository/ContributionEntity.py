from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Contribution(base):
    __tablename__ = 'Contributions'

    authorID = Column(BigInteger, ForeignKey("Authors.authorID"), primary_key=True)
    paperID = Column(BigInteger, ForeignKey("Papers.paperID"), primary_key=True)

    def __str__(self):
        return str(self.authorID) + " " + str(self.paperID)


class ContributionRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, authorID, paperID):
        contribution = Contribution(authorID=authorID, paperID=paperID)
        self.__session.add(contribution)
        self.__session.commit()

    def read(self):
        contributionList = []
        contributions = self.__session.query(Contribution)
        for contribution in contributions:
            contributionList.append(contribution)
        return contributionList

    def find_one(self, authorID, paperID):
        return self.__session.query(Contribution).filter(Contribution.authorID == authorID).filter(Contribution.paperID == paperID).one()

    def find_by_author(self, authorID):
        paperIDs = []
        contribuitons = self.__session.query(Contribution).filter(Contribution.authorID == authorID)
        for contrib in contribuitons:
            paperIDs.append(contrib.paperID)
        return paperIDs

    def update(self, authorID, paperID):
        pass

    def delete(self, authorID, paperID):
        contribution = self.find_one(authorID, paperID)
        self.__session.delete(contribution)
        self.__session.commit()
