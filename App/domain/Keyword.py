class Keyword:
    def __init__(self, keywordID: int, keyword: str):
        self.__keywordID = keywordID
        self.__keyword = keyword

    @property
    def keywordID(self) -> int:
        return self.__keywordID

    @keywordID.setter
    def keywordID(self, keywordID: int) -> None:
        self.__keywordID = keywordID

    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str) -> None:
        self.__keyword = keyword
