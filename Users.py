from notification.Notification import Notification
from notification.Notifier import Notifier
from post.PostFactory import PostFactory


# todo: add description

class Users(Notifier):
    __password_encode = None
    __connected = None
    __following = None
    __post = None

    # todo: add description
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.followers = 0
        self.notification = Notification()
        self.__password_encode = password.encode('utf-8')
        self.__connected = True
        self.__following = set()
        self.__posts = list()

    # Special method being overridden, creating custom String for printing
    def __str__(self):
        num_posts = len(
            self.__posts)  # Getting the length of the post list, it's the number of posts the notifier published
        return f"User name: {self.username}, Number of posts: {num_posts}, Number of followers: {self.get_num_subscriber()}"

    # Password Validation. using decode for compression
    def password_validation(self, password):
        try:
            if 4 < len(password) <= 8:  # Layer of protection before decoding the original password
                raise WrongPassword
            temp_pass = self.__password_encode.decode('utf-8')
            if temp_pass != password:  # Comparing the password
                raise WrongPassword
            return True
        except (WrongPassword, Exception) as e:
            print(e)

    # check the connection value, for encapsulation, and understandable code
    def is_connected(self):
        return self.__connected

    # Changing the connection value, for encapsulation, and understandable code
    def connect(self, password):
        try:
            if password_validation(password) is False:
                raise WrongPassword
            self.__connected = True
            return True
        except (WrongPassword, Exception) as e:
            print(e)

    # Changing the connection value, for encapsulation, and understandable code
    def disconnect(self, username):
        try:
            if self.username is not username:
                raise WrongUsername
            self.__connected = False
            return True
        except (WrongUsername, Exception) as e:
            print(e)

    # Follow method, add to following set and adding to the subscribers
    def follow(self, user):
        try:
            if self.__follow_exceptions(user):  # Exceptions Handling: self connected, user None, self is user
                pass
            if user.username in self.__following:  # Check self not following notifier Already
                raise AlreadyFollowingError(user.username)
            self.__following.add(user.username)  # Add to following List
            user.add_subscriber(
                self)  # adding self from user subscriber list(users to notify by user actions)            print(f"{str(self.username)} started following {user.username}")  # printing the follow action
        except (AlreadyFollowingError, Exception) as e:
            print(e)

    # UnFollow method,remove from the following set and removing from the subscribers
    def unfollow(self, user):
        try:
            if self.__follow_exceptions(user):  # Exceptions Handling: self connected, user None, self is user
                pass
            if user.username not in self.__following:  # Check self not following notifier Already
                raise NotFollowingError(user.username)
            self.__following.remove(user.username)  # Remove from following List
            user.remove_subscriber(self)  # Remove self from user subscriber list(users to notify by user actions)
            print(f"{self.username} unfollowed {user.username}")  # printing the unfollow action
        except (NotFollowingError, Exception) as e:
            print(e)

    # todo: add description
    def publish_post(self, post_type, *args):
        try:  # try Exceptions to make sure the program won't stop after encounter problem
            if not self.is_connected:  # Exception: Case User Not Connected
                raise NotConnectedError(self.username)
            post = PostFactory.create_post(self, post_type, *args)  # Creating the post
            self.__posts.append(post)  # Adding to the posts list
            self.notify_all_subscriber(f"{self.username} has a new post")  # Sending notification to all the subscribers
            return post  # Returning the post object
        except (NotConnectedError, Exception) as e:
            print(e)

    # Printing all the personal notification that related to the post.
    def print_notifications(self):
        try:
            if not self.is_connected():  # User Connected
                raise NotConnectedError(self.username)
            self.notification.display_notification(self.username)
        except (NotConnectedError, Exception) as e:
            print(e)

    # Exception handling, for follow or unfollow methods
    def __follow_exceptions(self, user):
        try:  # Exceptions Handling: self connected, user None, self is user
            if not self.is_connected():  # User Connected
                raise NotConnectedError(self.username)
            elif user is None:  # User None
                raise UserNotDefinedError
            elif self.username == user.username:  # User is Self
                raise UserSubscribeItSelf
        except (NotConnectedError, UserNotDefinedError, UserSubscribeItSelf, Exception) as e:
            print(e)
