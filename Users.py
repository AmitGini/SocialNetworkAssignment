class Users:
    _username = None
    _password = None
    _connected = None
    _followers = None
    _posts = None

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._connected = True
        self._followers = set()
        # self._posts = dict()

    def check_password(self, password):
        if self._password == password:
            return True
        else:
            return False

    def is_connected(self):
        return self._connected

    def get_username(self):
        return self._username

    def connect(self):
        self._connected = True
        print("Entered the connect method in Users class")

    def disconnect(self):
        self._connected = False
        print("Entered the disconnect method in Users class")

    def follow(self, user):
        # Since it's a set, there is no duplicate values, so there is no need to check if the user already following
        self._followers.add(user.get_username())
        print(self._username + " has followed " + user.get_username())

    def unfollow(self, user):
        # Since it's a set, there is no duplicate values, so there is no neet to check if the user already following
        # username The validation of the username, done in the SocialNetwork
        if user in self._followers:
            self._followers.remove(user.get_username())
            print(self._username + " has unfollowed " + user.get_username())


