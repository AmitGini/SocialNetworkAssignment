from CustomErrors import NotConnectedError, AlreadyLikedError, EmptyCommentError


# todo: add description
class Posts:
    _user = None
    _post_data = None
    _likes = None
    _comments = None

    # todo: add description
    def __init__(self, user, data):
        self._user = user
        self._post_data = data
        self._likes = set()
        self._comments = list(tuple())

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
            if self._user.username != user.username:  # Notify if the user that liked and post publisher user are different
                self._user.notification.update(f'{user.username} liked your post')
                print(f"{user.username} liked your post")
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
            if self._user.username != user.username:  # Notify if the user of that commented and post publisher user are different
                self._user.notification.update(f"{user.username} commented on your post")
                print(f"notification to {self._user.username}: commented on your post: {comment_data}")
        except (NotConnectedError, EmptyCommentError, Exception) as e:  # catching specific exceptions
            print(e)
