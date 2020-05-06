from typing import List
from common.Domain.Topic import Topic
from common.Domain.Keyword import Keyword


class Paper:
    def __init__(self, paperID: int, name: str, metadata: str, keywords: List[Keyword], topics: List[Topic],
                 document: str):
        self.__paperID = paperID
        self.__name = name
        self.__metadata = metadata
        self.__keywords = keywords
        self.__topics = topics
        self.__document = document

    @property
    def paperID(self) -> int:
        return self.__paperID

    @paperID.setter
    def paperID(self, value: int) -> None:
        self.__paperID = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def metadata(self) -> str:
        return self.__metadata

    @metadata.setter
    def metadata(self, value: str) -> None:
        self.__metadata = value

    @property
    def keywords(self) -> List[Keyword]:
        return self.__keywords

    @keywords.setter
    def keywords(self, value: List[Keyword]) -> None:
        self.__keywords = value

    @property
    def topics(self) -> List[Topic]:
        return self.__topics

    @topics.setter
    def topics(self, value: List[Topic]) -> None:
        self.__topics = value

    @property
    def document(self) -> str:
        return self.__document

    @document.setter
    def document(self, value: str) -> None:
        self.__document = value
