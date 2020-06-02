from domain.User import User
from domain.Paper import Paper
from typing import List


class Author(User):
    def __init__(self, authorID: int, affiliation: str, isSpeaker: bool, papers: List[Paper], user: User):
        super().__init__(user.userID, user.email, user.password, user.name, user.username)
        self.__authorID = authorID
        self.__affiliation = affiliation
        self.__isSpeaker = isSpeaker
        self.__papers = papers
        self.__user = user

    @property
    def authorID(self) -> int:
        return self.__authorID

    @property
    def affiliation(self) -> str:
        return self.__affiliation

    @property
    def isSpeaker(self) -> bool:
        return self.__isSpeaker

    @authorID.setter
    def authorID(self, value: int) -> None:
        self.__authorID = value

    @affiliation.setter
    def affiliation(self, value: str) -> None:
        self.__affiliation = value

    @isSpeaker.setter
    def isSpeaker(self, value: bool) -> None:
        self.__isSpeaker = value

    @property
    def papers(self) -> List[Paper]:
        return self.__papers

    @papers.setter
    def papers(self, value: List[Paper]) -> None:
        self.__papers = value

    @property
    def user(self) -> User:
        return self.__user