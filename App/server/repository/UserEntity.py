from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import BigInteger

db_string = "postgres://postgres:password@localhost:5432/ConfSys"

db = create_engine(db_string)
base = declarative_base()


class User(base):
    __tablename__ = 'Users'

    userID = Column(BigInteger, primary_key=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    username = Column(String)

    def __str__(self):
        return str(self.userID) + " " + self.email + " " + self.password + " " + self.name + " " + self.username



class UserRepository:
    def __init__(self):
        Session = sessionmaker(db)
        self.__session = Session()

        base.metadata.create_all(db)

    def add(self, userID, email, password, name, username):
        user = User(userID=userID, email=email, password=password, name=name, username=username)
        self.__session.add(user)
        self.__session.commit()

    def read(self):
        userList = []
        users = self.__session.query(User)
        for user in users:
            userList.append(user)
        return userList

    def find_one(self, userID):
        return self.__session.query(User).filter(User.userID==userID).one()

    def update(self, userID, email, password, name, username):
        user = self.find_one(userID)
        user.email = email
        user.password = password
        user.name = name
        user.username = username
        self.__session.commit()

    def delete(self, userID):
        user = self.find_one(userID)
        self.__session.delete(user)
        self.__session.commit()

'''
userRepo = UserRepository()
users = userRepo.read()
for user in users:
    print(user)

user1=userRepo.find_one(1)
print(user1)
'''
