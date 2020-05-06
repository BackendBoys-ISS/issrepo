class Bid:
    def __init__(self, result: int, paperID: int, reviewerID: int):
        self.__result = result
        self.__paperID = paperID
        self.__reviewerID = reviewerID

    @property
    def result(self) -> int:
        return self.__result

    @result.setter
    def result(self, value) -> None:
        self.__result = value

    @property
    def paperID(self) -> int:
        return self.__paperID

    @paperID.setter
    def paperID(self, value) -> None:
        self.__paperID = value

    @property
    def reviewerID(self) -> int:
        return self.__reviewerID

    @reviewerID.setter
    def reviewerID(self, value: int) -> None:
        self.__reviewerID = value