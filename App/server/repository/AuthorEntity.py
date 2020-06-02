from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger, Boolean, String

db_string = "postgres://postgres:password@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Author(base):
    __tablename__ = 'Authors'

    authorID = Column(BigInteger, primary_key=True)
    userID = Column(BigInteger, ForeignKey("Users.userID"))
    affiliation = Column(String)
    isSpeaker = Column(Boolean)

    def __str__(self):
        return str(self.authorID) + " " + str(self.userID) + " " + self.affiliation + " " + str(self.isSpeaker)


class AuthorRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, authorID, userID, affiliation, isSpeaker):
        author = Author(authorID=authorID, userID=userID, affiliation=affiliation, isSpeaker=isSpeaker)
        self.__session.add(author)
        self.__session.commit()

    def read(self):
        authorList = []
        authors = self.__session.query(Author)
        for author in authors:
            authorList.append(author)
        return authorList

    def find_one(self, authorID):
        return self.__session.query(Author).filter(Author.authorID == authorID).one()

    def find_one_by_userID(self, userID):
        return self.__session.query(Author).filter(Author.userID == userID).one()

    def update(self,authorID, userID, affiliation, isSpeaker):
        author = self.find_one(authorID)
        author.userID = userID
        author.affiliation = affiliation
        author.isSpeaker = isSpeaker
        self.__session.commit()

    def delete(self, authorID):
        author = self.find_one(authorID)
        self.__session.delete(author)
        self.__session.commit()
