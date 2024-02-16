from PostFactory import PostFactory

# todo: add description
class Users:
    # todo: add description
    __username = None
    __password = None
    __connected = None
    __followers = None
    __posts = None

    # todo: add description
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__connected = True
        self.__followers = set()
        self.__posts = list()

    # Special method being overridden, to print the data as required.
    def __str__(self):
        num_posts = len(self.__posts)
        num_followers = len(self.__followers)
        return ("User name: {username}, Number of posts: {num_posts}, Number of followers: {num_followers}"
                .format(username=self.__username, num_posts=num_posts,num_followers=num_followers))

    # todo: add description
    def check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

    # todo: add description
    def get_username(self):
        return self.__username

    # todo: add description
    def connect(self):
        self.__connected = True

    # todo: add description
    def disconnect(self):
        self.__connected = False

    # todo: add description
    def is_connected(self):
        return self.__connected

    # todo: add description
    def follow(self, user):
        if self.__connected:
            if user.get_username() in self.__followers:
                print("{follower} already follow {followed}".format(follower=self.__username,
                                                                    followed=user.get_username()))
            # Since it's a set, there is no duplicate values, so there is no need to check if the user already following
            else:
                self.__followers.add(user.get_username())
                print("{follower} started following {followed}".format(follower=self.__username,
                                                              followed=user.get_username()))
        else:
            print("{username} Not Connected!".format(username=self.__username))  # case where user try to use
            # function while is not connected

    # todo: add description
    def unfollow(self, user):
        if self.__connected:
            # Since it's a set, there is no duplicate values, so there is no neet to check if the user already following
            # username The validation of the username, done in the SocialNetwork
            if user.get_username() in self.__followers:
                self.__followers.remove(user.get_username())
                print("{follower} unfollowed {followed}".format(follower=self.__username,
                                                                followed=user.get_username()))
            else:
                print("{follower} did not followed {followed}".format(follower=self.__username,
                                                                      followed=user.get_username()))
        else:
            print("{username} Not Connected!".format(username=self.__username))  # case where user try to use function while is not connected

    # todo: add description
    def publish_post(self, post_type, *args):
        if self.__connected:
            post = PostFactory.create_post(self, post_type, *args)
            if post is not None:
                self.__posts.append(post)
                print(post)
                return post
            else:
                print("Try Again!")
                return None
        else:
            print("{username} Not Connected!".format(username=self.__username))
            return None


    # todo: DESCRIPTION
    def print_notifications(self):
        # todo: INIT FUNCTION
        print("NOTIFICATION: Function Need to be Added")
