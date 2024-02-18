from error.NotConnectedError import NotConnectedError
from error.UserActionsError import UserActionsError


# todo: add description
class Posts:

    # todo: add description
    def __init__(self, user, data):
        self._user = user
        self.publisher_username = self._user.username
        self._post_data = data
        self._likes = set()
        self._comments = list(tuple())

    def __str__(self):
        pass

    # todo: add description
    def like(self, user):
        if user.is_connected:
            if user.username not in self._likes:
                self._likes.add(user.username)
                if self._user.username != user.username:
                    message = f"{user.username} liked your post"
                    self._user.notification.update(message)
                    print(f"notification to {self._user.username}: {message}")
            else:
                raise UserActionsError("RepeatLike")
        else:
            raise NotConnectedError()


    # todo: DESCRIPTION
    def comment(self, user, comment_data):
        if user.is_connected:
            if comment_data is not None:
                self._comments.append((user.username, comment_data))
                if self._user.username != user.username:
                    message = f"{user.username} commented on your post"
                    self._user.notification.update(message)
                    print(f"notification to {self._user.username}: {message}: {comment_data}")
            else:
                raise UserActionsError("EmptyComment")
        else:
            raise NotConnectedError()




