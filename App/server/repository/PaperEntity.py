from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger

db_string = "postgres://postgres:admin@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Paper(base):
    __tablename__ = 'Papers'

    paperID = Column(BigInteger, primary_key=True)
    name = Column(String)
    metadataa = Column(String)
    document = Column(String)

    def __str__(self):
        return str(self.paperID) + " " + self.name + " " + self.metadataa + " " + self.document


class PaperRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, paperID, name, metadataa, document):
        paper = Paper(paperID=paperID, name=name, metadataa=metadataa, document=document)
        self.__session.add(paper)
        self.__session.commit()

    def read(self):
        paperList = []
        papers = self.__session.query(Paper)
        for paper in papers:
            paperList.append(paper)
        return paperList

    def find_one(self, paperID):
        return self.__session.query(Paper).filter(Paper.paperID == paperID).one()

    def update(self, paperID, name, metadataa, document):
        paper = self.find_one(paperID)
        paper.name = name
        paper.metadataa = metadataa
        paper.document = document
        self.__session.commit()

    def delete(self, paperID):
        paper = self.find_one(paperID)
        self.__session.delete(paper)
        self.__session.commit()


