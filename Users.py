from CustomErrors import WrongPassword, WrongUsername, AlreadyFollowingError, NotFollowingError, NotConnectedError, \
    UserNotDefinedError, UserSubscribeItSelf
from Notification import Notification
from NotificationService import NotificationService
from PostFactory import PostFactory


# User Class, representing the users that signed up to the Social Network
class Users(NotificationService):
    __password_encode = None
    __connected = None
    __following = None
    __post = None

    # User constructor, holding its data username and coded password, connection status, list of posts,
    # users that he follow using set, and notification object that responsible to update the user subscribers
    def __init__(self, username, password):
        super().__init__()
        self.username = username
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
            if 4 > len(password) > 8:  # Layer of protection before decoding the original password
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
            if self.password_validation(password) is False:
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

    # Follow method, when self(user) use follow, the followed user being added to the following set
    # And self being added to the subscribers set of the user he followed after for notification updates
    def follow(self, user):
        try:
            if self.__follow_exceptions(user):  # Exceptions Handling: self connected, user None, self is user
                pass
            if user.username in self.__following:  # Check self not following notifier Already
                raise AlreadyFollowingError(user.username)
            self.__following.add(user.username)  # Add to following List
            user.add_subscriber(self)  # adding self from user subscriber list(users to notify by user actions)
            print(f"{str(self.username)} started following {user.username}")  # printing the follow action
        except (AlreadyFollowingError, Exception) as e:
            print(e)

    # Unfollow method, when self(user) use unfollow, the unfollowed user being removed from the following set
    # And self being removed from the subscribers set of the user he unfollowed, and won't be notified anymore
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

    # method for publishing a post in Social Network by the user, if the user is connected
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

    # Printing all the notification that related to the post.
    def print_notifications(self):
        try:
            if not self.is_connected():  # User Connected
                raise NotConnectedError(self.username)
            self.notification.display_notification(self.username)
        except (NotConnectedError, Exception) as e:
            print(e)

    # Private method that handling the Exception, for follow or unfollow methods
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
