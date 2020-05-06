class Room:
    def __init__(self, roomID: int, name: str, seatNo: int):
        self.__roomID = roomID
        self.__name = name
        self.__seatNo = seatNo

    @property
    def roomID(self) -> int:
        return self.__roomID

    @roomID.setter
    def roomID(self, value: int) -> None:
        self.__roomID = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def seatNo(self) -> int:
        return self.__seatNo

    @seatNo.setter
    def seatNo(self, value: int) -> None:
        self.__seatNo = value
