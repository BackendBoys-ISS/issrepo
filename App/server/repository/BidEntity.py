from sqlalchemy import create_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger, Integer

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Bid(base):
    __tablename__ = 'Bids'

    memberID = Column(BigInteger, ForeignKey("PCmembers.memberID"), primary_key=True)
    paperID = Column(BigInteger, ForeignKey("Papers.paperID"), primary_key=True)
    result = Column(Integer)

    def __str__(self):
        return str(self.memberID) + " " + str(self.paperID) + " " + str(self.result)


class BidRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, memberID, paperID, result):
        bid = Bid(memberID=memberID, paperID=paperID, result=result)
        self.__session.add(bid)
        self.__session.commit()

    def read(self):
        bidList = []
        bids = self.__session.query(Bid)
        for bid in bids:
            bidList.append(bid)
        return bidList

    def find_one(self, memberID, paperID):
        return self.__session.query(Bid).filter(Bid.memberID == memberID).filter(Bid.paperID == paperID).one()

    def update(self, memberID, paperID, result):
        bid = self.find_one(memberID, paperID)
        bid.result = result
        self.__session.commit()

    def delete(self, memberID, paperID):
        bid = self.find_one(memberID, paperID)
        self.__session.delete(bid)
        self.__session.commit()
