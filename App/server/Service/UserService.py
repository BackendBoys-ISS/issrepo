from server.repository.UserEntity import UserRepository


class UserService:
    def __init__(self):
        self.__userRpo = UserRepository()
        self.__baseID = 77

    def create_account(self, email, password, name, username):
        try:
            self.__userRpo.add(self.__baseID, email, password, name, username)
            self.__baseID += 1
            return True
        except:
            return False

    def login(self, email, password):
        user = self.__userRpo.find_by_email_pass(email, password)
        if user is None:
            return None
        return user.userID

