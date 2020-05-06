from common.Domain.Program import Program
from datetime import date


class Conference:
    def __init__(self, conferenceID: int, conferenceName: str, startingDate: date, endingDate: date,
                 abstractDeadline: date, proposalDeadline: date, biddingDeadline: date, program: Program):
        self.__conferenceID = conferenceID
        self.__conferenceName = conferenceName
        self.__startingDate = startingDate
        self.__endingDate = endingDate
        self.__abstractDeadline = abstractDeadline
        self.__proposalDeadline = proposalDeadline
        self.__biddingDeadline = biddingDeadline
        self.__program = program

    @property
    def conferenceID(self) ->  int:
        return self.__conferenceID

    @conferenceID.setter
    def conferenceID(self, value: int) -> None:
        self.__conferenceID = value

    @property
    def conferenceName(self) -> str:
        return self.__conferenceName

    @conferenceName.setter
    def conferenceName(self, value: str) -> None:
        self.__conferenceName = value

    @property
    def startingDate(self) -> date:
        return self.__startingDate

    @startingDate.setter
    def startingDate(self, value: date) -> None:
        self.__startingDate = value

    @property
    def endingDate(self) -> date:
        return self.__endingDate

    @endingDate.setter
    def endingDate(self, value: date) -> None:
        self.__endingDate = value

    @property
    def abstractDeadline(self) -> date:
        return self.__abstractDeadline

    @abstractDeadline.setter
    def abstractDeadline(self, value) -> None:
        self.__abstractDeadline = value

    @property
    def proposalDeadline(self) -> date:
        return self.__proposalDeadline

    @proposalDeadline.setter
    def proposalDeadline(self, value: date) -> None:
        self.__proposalDeadline = value

    @property
    def biddingDeadline(self) -> date:
        return self.__biddingDeadline

    @biddingDeadline.setter
    def biddingDeadline(self, value: date) -> None:
        self.__biddingDeadline = value

    @property
    def program(self) -> Program:
        return self.__program

    @program.setter
    def program(self, value: Program) -> None:
        self.__program = value