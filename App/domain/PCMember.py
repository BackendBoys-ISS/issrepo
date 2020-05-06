from common.Domain.Author import Author


class PCMember(Author):
    def __init__(self, memberID: int, website: str, isChair: bool, author: Author):
        super().__init__(author.authorID, author.affiliation, author.isSpeaker, author.papers, author.user)
        self.__memberID = memberID
        self.__website = website
        self.__isChair = isChair
        self.__author = author

    @property
    def memberID(self) -> int:
        return self.__memberID

    @memberID.setter
    def memberID(self, value: int) -> None:
        self.__memberID = value

    @property
    def website(self) -> str:
        return self.__website

    @website.setter
    def website(self, value: str) -> None:
        self.__website = value

    @property
    def isChiar(self) -> bool:
        return self.__isChair

    @isChiar.setter
    def isChiar(self, value: bool) -> None:
        self.__isChair = value

    @property
    def author(self) -> Author:
        return self.__author
