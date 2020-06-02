class Topic:
    def __init__(self, topicID: int, topic: str):
        self.__topicID = topicID
        self.__topic = topic

    def __str__(self):
        return self.__topic

    @property
    def topicID(self):
        return self.__topicID

    @topicID.setter
    def topicID(self, topicID):
        self.__topicID = topicID

    @property
    def topic(self):
        return self.__topic

    @topic.setter
    def topic(self, topic):
        self.__topic = topic
