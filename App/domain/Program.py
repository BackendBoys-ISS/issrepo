from datetime import date
from datetime import time


class Program:
    def __init__(self, calendarDate: date, hoursInterval: time):
        self.__calendarDate = calendarDate
        self.__hoursInterval = hoursInterval

    @property
    def calendarDate(self) -> date:
        return self.__calendarDate

    @calendarDate.setter
    def calendarDate(self, value: date):
        self.__calendarDate = value

    @property
    def hoursInterval(self) -> time:
        return self.__hoursInterval

    @hoursInterval.setter
    def hoursInterval(self, value: time):
        self.__hoursInterval = value
