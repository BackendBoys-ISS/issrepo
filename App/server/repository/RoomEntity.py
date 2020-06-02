from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger, Integer

db_string = "postgres://postgres:password@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class Room(base):
    __tablename__ = 'Rooms'

    roomID = Column(BigInteger, primary_key=True)
    name = Column(String)
    seatNo = Column(Integer)

    def __str__(self):
        return str(self.roomID) + " " + self.name + " " + self.seatNo


class RoomRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, roomID, name, seatNo):
        room = Room(roomID=roomID, name=name, seatNo=seatNo)
        self.__session.add(room)
        self.__session.commit()

    def read(self):
        roomList = []
        rooms = self.__session.query(Room)
        for room in rooms:
            roomList.append(room)
        return roomList

    def find_one(self, roomID):
        return self.__session.query(Room).filter(Room.roomID == roomID).one()

    def update(self, roomID, name, seatNo):
        room = self.find_one(roomID)
        room.roomID = roomID
        room.name = name
        room.seatNo = seatNo
        self.__session.commit()

    def delete(self, roomID):
        room = self.find_one(roomID)
        self.__session.delete(room)
        self.__session.commit()
