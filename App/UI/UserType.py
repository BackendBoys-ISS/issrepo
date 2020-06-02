class UserType:
    def __init__(self, isOnlyAuthor: bool, isSpeaker: bool, isListener: bool, username: str):
        self.isOnlyAuthor = isOnlyAuthor
        self.isSpeaker = isSpeaker
        self.isListener = isListener
        self.username = username
