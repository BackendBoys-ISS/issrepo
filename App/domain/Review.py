class Review:
    def __init__(self, result: int, reviewerID: int, paperID: int, evaluation: str):
        self.__result = result
        self.__reviewerID = reviewerID
        self.__paperID = paperID
        self.__evaluation = evaluation

    @property
    def result(self) -> int:
        return self.__result

    @result.setter
    def result(self, value) -> None:
        self.__result = value

    @property
    def reviewerID(self) -> int:
        return self.__reviewerID

    @reviewerID.setter
    def reviewerID(self, value) -> None:
        self.__reviewerID = value

    @property
    def paperID(self) -> int:
        return self.__paperID

    @paperID.setter
    def paperID(self, value) -> None:
        self.__paperID = value

    @property
    def evaluation(self) -> str:
        return self.__evaluation

    @evaluation.setter
    def evaluation(self, value: str) -> None:
        self.__evaluation = value
