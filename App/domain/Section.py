from common.Domain.Program import Program
from typing import List


class Section:
    def __init__(self, sectionID: int, supervisorID: int, roomID: int, speakerID: List[int],
                 conferenceID: int, program: Program):
        self.__sectionID = sectionID
        self.__supervisorID = supervisorID
        self.__roomID = roomID
        self.__speakerID = speakerID
        self.__conferenceID = conferenceID
        self.__program = program
    
    @property
    def sectionID(self) -> int:
        return self.__sectionID
    
    @sectionID.setter
    def sectionID(self, value: int) -> None:
        self.__sectionID = value
        
    @property
    def supervisorID(self) -> int:
        return self.__supervisorID
    
    @supervisorID.setter
    def supervisorID(self, value: int) -> None:
        self.__supervisorID = value
        
    @property
    def roomID(self) -> int:
        return self.__roomID
    
    @roomID.setter
    def roomID(self, value: int) -> None:
        self.__roomID = value
        
    @property
    def speakerID(self) -> List[int]:
        return self.__speakerID
    
    @speakerID.setter
    def speakerID(self, value) -> None:
        self.__speakerID = value
        
    @property
    def conferenceID(self) -> int:
        return self.__conferenceID
    
    @conferenceID.setter
    def conferenceID(self, value: int) -> None:
        self.__conferenceID = value

    @property
    def program(self) -> Program:
        return self.__program

    @program.setter
    def program(self, value: Program):
        self.__program = value
