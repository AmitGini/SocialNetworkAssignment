import Users
from CustomErrors import NotConnectedError, AlreadyLikedError, EmptyCommentError
from abc import ABC, abstractmethod


# Interface Post Class, representing general post methods and fields.
class Post(ABC):
    _author = None
    _post_data = None
    _likes = None
    _comments = None

    # Initializes a new post instance with the given user and data.
    def __init__(self, author, data):
        """
        :param _author: protected field of The user who created the post.
        :param _data: protected field of The content of the post
        :param _likes: protected field of Set of the usernames that like the post
        :param _comments: protected field of list of tuples, every tuple contain (string=username, string=comment)
        """
        self._author = author  # user of Users class
        self._post_data: dict = data
        self._likes: set = set()
        self._comments: list[tuple] = list(tuple())

    @abstractmethod
    def __str__(self):
        pass

    # Adding like to the post and notify the post publisher(user)
    def like(self, user):
        try:  # try Exceptions to make sure the program won't stop after encounter problem
            if not user.is_connected:  # Exceptions: Connection Validation
                raise NotConnectedError(user.username)
            if user.username in self._likes:  # Exceptions:  User already Liked the Post
                raise AlreadyLikedError(user.username)
            self._likes.add(user.username)  # Adding Like to the list of the post comments
            if self._author.username != user.username:  # Notify if the user that liked and post publisher user are different
                self._author.notification.update(f'{user.username} liked your post')
                print(f"notification to {self._author.username}: {user.username} liked your post")
        except (NotConnectedError, AlreadyLikedError, Exception) as e:  # catching specific exceptions
            print(e)

    # Adding comment to the post and notify the post publisher(user)
    def comment(self, user, comment_data):
        try:  # try Exceptions to make sure the program won't stop after encounter problem
            if not user.is_connected:  # Exceptions: Connection Validation
                raise NotConnectedError(user.username)
            if comment_data is None:  # Exceptions:  Comment data is empty
                raise EmptyCommentError
            self._comments.append((user.username, comment_data))  # Adding Comment to the list of the post comments
            if self._author.username != user.username:  # Notify if the user of that commented and post publisher user are different
                self._author.notification.update(f"{user.username} commented on your post")
                print(f"notification to {self._author.username}: {user.username} commented on your post: {comment_data}")
        except (NotConnectedError, EmptyCommentError, Exception) as e:  # catching specific exceptions
            print(e)
