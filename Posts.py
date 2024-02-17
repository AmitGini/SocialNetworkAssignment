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

    # todo: add description
    def like(self, user):
        if user.is_connected:
            if user.username not in self._likes:
                self._likes.add(user.username)
                self._user.notification.update("{user} liked your post".format(user=user.username))
            else:
                raise UserActionsError("RepeatLike")
        else:
            raise NotConnectedError()


    # todo: DESCRIPTION
    def comment(self, user, comment_data):
        if user.is_connected:
            if comment_data is not None:
                self._comments.append((user.username, comment_data))
                self._user.notification.update("{user} commented on your post".format(user=user.username))
            else:
                raise UserActionsError("EmptyComment")
        else:
            raise NotConnectedError()

    def __str__(self):
        pass


