from sqlalchemy import create_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger, Integer

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Review(base):
    __tablename__ = 'Reviews'

    memberID = Column(BigInteger, ForeignKey("PCmembers.memberID"), primary_key=True)
    paperID = Column(BigInteger, ForeignKey("Papers.paperID"), primary_key=True)
    result = Column(Integer)
    evaluation = Column(String)

    def __str__(self):
        return str(self.memberID) + " " + str(self.paperID) + " " + str(self.result) + " " +\
               self.evaluation


class ReviewRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, memberID, paperID, result, evaluation):
        review = Review(memberID=memberID, paperID=paperID, result=result, evaluation=evaluation)
        self.__session.add(review)
        self.__session.commit()

    def read(self):
        reviewList = []
        reviews = self.__session.query(Review)
        for review in reviews:
            reviewList.append(review)
        return reviewList

    def find_one(self, memberID, paperID):
        return self.__session.query(Review).filter(Review.memberID == memberID).filter(Review.paperID == paperID).one()

    def update(self, memberID, paperID, result, evaluation):
        review = self.find_one(memberID, paperID)
        review.result = result
        review.evaluation = evaluation
        self.__session.commit()

    def delete(self, memberID, paperID):
        review = self.find_one(memberID, paperID)
        self.__session.delete(review)
        self.__session.commit()
