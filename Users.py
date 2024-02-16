from PostFactory import PostFactory


class Users:
    __username = None
    __password = None
    __connected = None
    __followers = None
    __posts = None

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__connected = True
        self.__followers = set()
        self.__posts = list()

    def check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

    def is_connected(self):
        return self.__connected

    def get_username(self):
        return self.__username

    def connect(self):
        self.__connected = True

    def disconnect(self):
        self.__connected = False

    def follow(self, user):
        # Since it's a set, there is no duplicate values, so there is no need to check if the user already following
        self.__followers.add(user.get_username())
        print(self.__username + " has followed " + user.get_username())

    def unfollow(self, user):
        # Since it's a set, there is no duplicate values, so there is no neet to check if the user already following
        # username The validation of the username, done in the SocialNetwork
        if user in self.__followers:
            self.__followers.remove(user.get_username())
            print(self.__username + " has unfollowed " + user.get_username())

    def publish_post(self, post_type, *args):
        if args is not None and len(args) > 0:
            post = PostFactory.create_post(self, post_type, *args)
            self.__posts.append(post)
            return post
        return None
