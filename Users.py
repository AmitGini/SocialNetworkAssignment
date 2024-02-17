from error.NotConnectedError import NotConnectedError
from error.UserActionsError import UserActionsError
from notification.Notification import Notification
from notification.Notifier import Notifier
from post.PostFactory import PostFactory


class Users(Notifier):

    # todo: add description
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.notification = Notification()
        self.__password_encode = password.encode('utf-8')
        self.__connected = True
        self.__follow = set()
        self.__posts = list()


    # Special method being overridden, to print the data as required.
    def __str__(self):
        num_posts = len(self.__posts)
        num_followers = len(self.__follow)
        return ("User name: {username}, Number of posts: {num_posts}, Number of followers: {num_followers}"
                .format(username=self.username, num_posts=num_posts, num_followers=num_followers))

    # todo: add description
    def check_password(self, password):
        # Layer of protection before decoding the original password
        if 0 < len(password) <= 8:
            temp_pass = self.__password_encode.decode('utf-8')
            # Comparing the password
            if temp_pass == password:
                return True
            else:
                return False

    # check the connection value, for encapsulation, and understandable code
    def is_connected(self):
        return self.__connected

    # Changing the connection value, for encapsulation, and understandable code
    def connect(self):
        self.__connected = True

    # Changing the connection value, for encapsulation, and understandable code
    def disconnect(self):
        self.__connected = False

    # todo: add description
    def follow(self, user):
        # Exceptions Handling:
        if self.__follow_exceptions(user, "follow"):
            pass
        # Follow
        else:
            # Add to following List
            self.__follow.add(user.username)
            # Adding self to user Watcher list
            # self will be notified when user publish a post
            user.notification.update(f"{self.username} has started following you.")
            user.add_watcher(self)
            print("{follower} started following {followed}".format(follower=self.username,
                                                                   followed=user.username))

        # todo: add description
    def unfollow(self, user):
        # Exceptions Handling:
        if self.__follow_exceptions(user, "unfollow"):
            pass
        # UnFollow
        else:
            # Remove from following List
            self.__follow.remove(user.username)
            # Remove self from user watcher list
            # self will not be notified when user publish a post
            user.remove_watcher(self)
            print("{follower} unfollowed {followed}".format(follower=self.username,
                                                            followed=user.username))

    # todo: add description
    def publish_post(self, post_type, *args):
        # Case Not Connected
        if not self.is_connected:
            raise NotConnectedError()

        # Case connected
        else:
            # Handle None argument in post creation
            post = PostFactory.create_post(self, post_type, *args)
            # Added to the posts list
            self.__posts.append(post)
            # Sending Notification to all the watcher/followers of mine
            self.notify_all_watchers("{username} has a new post".format(username=self.username))
            print(post)
            return post

    # todo: add description
    def print_notifications(self):
        self.notification.display_notification(self.username)

    # todo: add description
    def __follow_exceptions(self, user, follow_type):
        # General Cases
        # User Connected
        if not self.is_connected():
            raise NotConnectedError()
            # User None
        elif user is None:
            raise UserActionsError("NotExist")

        # Follow Case:
        # Follow itself
        if follow_type == "follow":
            if user.username is self.username:
                raise UserActionsError("FollowSelf")
            # Follow already being followed
            if user.username in self.__follow:
                raise UserActionsError("FollowedAlready")

            # UnFollow Case:
        else:
            # UnFollow itself
            if user.username is self.username:
                raise UserActionsError("UnfollowSelf")
            # Not in the Following list, so cant be removed
            if user.username not in self.__follow:
                raise UserActionsError("NotFollowed")
