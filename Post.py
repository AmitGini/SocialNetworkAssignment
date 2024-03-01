from CustomErrors import NotConnectedError, AlreadyLikedError, EmptyCommentError
from abc import ABC, abstractmethod


# Structure Design pattern
# Interface Post Class, representing general post methods and fields.
class Post(ABC):

    # Initializes a new post instance with the given user and data.
    def __init__(self, author):
        self._author = author  # owner of the post
        self._likes: set = set()  # set of all the usernames that liked this post
        self._comments: list[tuple] = list(tuple())  # list of tuples, every tuple contain (string=username, string=comment)

    @abstractmethod
    def __str__(self):
        pass

    # Adding like to the post and notify the post publisher(user)
    def like(self, user):
        try:  # try Exceptions to make sure the program won't stop after encounter problem
            if not user.is_connected:  # Exceptions: Connection Validation
                raise NotConnectedError(user.username)
            elif user.username in self._likes:  # Exceptions:  User already Liked the Post
                raise AlreadyLikedError(user.username)
            else:
                self._likes.add(user.username)  # Adding Like to the list of the post comments
                if self._author.username != user.username:  # Notify if the user that liked and post publisher user are different
                    self._author.update(f'{user.username} liked your post')  # Sending update(notification) to author
                    print(f"notification to {self._author.username}: {user.username} liked your post")  # printing
        except (NotConnectedError, AlreadyLikedError, Exception) as e:  # catching specific exceptions
            print(e)

    # Adding comment to the post and notify the post publisher(user)
    def comment(self, user, comment_data):
        try:  # try Exceptions to make sure the program won't stop after encounter problem
            if not user.is_connected:  # Exceptions: Connection Validation
                raise NotConnectedError(user.username)
            elif comment_data is None:  # Exceptions:  Comment data is empty
                raise EmptyCommentError
            else:
                self._comments.append((user.username, comment_data))  # Adding Comment to the list of the post comments
                if self._author.username != user.username:  # Notify if the user of that commented and post publisher user are different
                    self._author.update(f"{user.username} commented on your post")  # Sending update(notification) to author
                    print(f"notification to {self._author.username}: {user.username} commented on your post: {comment_data}")  # printing
        except (NotConnectedError, EmptyCommentError, Exception) as e:  # catching specific exceptions
            print(e)
