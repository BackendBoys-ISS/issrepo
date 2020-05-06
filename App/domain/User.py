class User:
    def __init__(self, userID: int, email: str, password: str, name: str, username: str):
        self.__userID = userID
        self.__email = email
        self.__password = password
        self.__name = name
        self.__username = username

    @property
    def userID(self) -> int:
        return self.__userID

    @property
    def email(self) -> str:
        return self.__email

    @property
    def password(self) -> str:
        return self.__password

    @property
    def name(self) -> str:
        return self.__name

    @property
    def username(self) -> str:
        return self.__username

    @userID.setter
    def userID(self, userID: int) -> None:
        self.__userID = userID

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    @password.setter
    def password(self, password: str) -> None:
        self.__password = password

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @username.setter
    def username(self, username) -> None:
        self.__username = username
