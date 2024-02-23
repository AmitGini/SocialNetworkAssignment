from CustomErrors import WrongPassword, WrongUsername, AlreadyFollowingError, NotFollowingError, NotConnectedError, \
    UserNotDefinedError, UserSubscribeItSelf
from PostPublisher import PostPublisher
from Subscriber import Subscriber
from PostFactory import PostFactory

'''                         
    # Observer Design Pattern                    
    # User Class - Implementing Subscriber(Subscriber interface - Observer)
    # representing the users in the social network, Users are Subscribers(Concrete Subscriber/Concrete Observer)
            user can be update his subscribers but also can be updated(notified) by other users depend on the action
            like/comment or publishing a post, user will be notify when other user publish a post only if he follow
            after that user means hes part of that author post subscribers 
'''


class Users(Subscriber):
    __notifications = None
    __password_encode = None
    __connected = None
    __following = None
    __post = None

    # User constructor, holding its data username and coded password, connection status, list of posts,
    # users that he follow using set, and notification object that responsible to update the user subscribers
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.post_publisher = PostPublisher()
        self.__password_encode = password.encode('utf-8')
        self.__connected = True
        self.__following = set()
        self.__posts = list()
        self.__notifications = list()

    # Special method being overridden, creating custom String for printing
    def __str__(self):
        num_posts = len(
            self.__posts)  # Getting the length of the post list, it's the number of posts the notifier published
        return f"User name: {self.username}, Number of posts: {num_posts}, Number of followers: {self.post_publisher.get_num_subscriber()}"

    # Password Validation. using decode for compression
    def password_validation(self, password):
        try:
            if 4 > len(password) > 8:  # Layer of protection before decoding the original password
                raise WrongPassword
            elif self.__password_encode.decode('utf-8') != password:  # Comparing the password
                raise WrongPassword
            else:
                return True
        except (WrongPassword, Exception) as e:
            print(e)
            return False

    # check the connection value, for encapsulation, and understandable code
    def is_connected(self):
        return self.__connected

    # Changing the connection value, for encapsulation, and understandable code
    def connect(self, password):
        if self.password_validation(password) is False:
            return False
        else:
            self.__connected = True
            return True

    # Changing the connection value, for encapsulation, and understandable code
    def disconnect(self, username):
        if self.username is not username:
            print(WrongUsername)
        else:
            self.__connected = False
            return True

    # Follow method, when self(user) use follow, the followed user being added to the following set
    # And self being added to the subscribers set of the user he followed after for notification updates
    def follow(self, user):
        try:
            if self.__follow_exceptions(user):  # Exceptions Handling: self connected, user None, self is user
                pass  # raise exception in the __follow_exceptions method
            elif user.username in self.__following:  # Check self not following notifier Already
                raise AlreadyFollowingError(user.username)
            else:
                self.__following.add(user.username)  # Add to following List
                user.post_publisher.add_subscriber(
                    self)  # adding self from user subscriber list(users to notify by user actions)
                print(f"{str(self.username)} started following {user.username}")  # printing the follow action
        except (AlreadyFollowingError, Exception) as e:
            print(e)

    # Unfollow method, when self(user) use unfollow, the unfollowed user being removed from the following set
    # And self being removed from the subscribers set of the user he unfollowed, and won't be notified anymore
    def unfollow(self, user):
        try:
            if self.__follow_exceptions(user):  # Exceptions Handling: self connected, user None, self is user
                pass
            elif user.username not in self.__following:  # Check self not following notifier Already
                raise NotFollowingError(user.username)
            else:
                self.__following.remove(user.username)  # Remove from following List
                user.post_publisher.remove_subscriber(
                    self)  # Remove self from user subscriber list(users to notify by user actions)
                print(f"{self.username} unfollowed {user.username}")  # printing the unfollow action
        except (NotFollowingError, Exception) as e:
            print(e)

    def publish_post(self, post_type, *args):
        try:
            if not self.is_connected:  # Check if the user is connected before proceeding.
                raise NotConnectedError
            post = PostFactory.create_post(self, post_type,
                                           *args)  # Attempt to create a new post of the specified type.
        except (Exception, NotConnectedError) as e:
            print(f"An unexpected error occurred while creating the post: {e}")
            return None

        # If post creation was unsuccessful, indicate failure.
        if post is None:
            print("Failed to create the post. Please check the post details and try again.")
            return None

        # Post creation was successful, proceed with adding to the user's posts and notifying subscribers.
        self.__posts.append(post)
        self.post_publisher.send_new_post_notification(self.username)
        return post

    # updating the user, by adding the message to its notification list
    def update(self, message):
        self.__notifications.append(message)

    # Iterate over the notification list and printing them from the first(oldest) to the last(newest)
    def print_notifications(self):
        try:
            if not self.is_connected():  # Check User Connected
                raise NotConnectedError(self.username)
            else:
                print(f"{self.username}'s notifications:")  # Printing tile
                for notification in self.__notifications:  # Printing all the notification the user received
                    print(notification)
        except (NotConnectedError, Exception) as e:  # Exception message
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
            return True
