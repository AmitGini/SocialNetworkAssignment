
# todo: add description
class Posts:
    # todo: add description
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

    # todo: add description
    def like(self, user):
        if user.is_connected:
            username_like = user.get_username()
            if username_like not in self._likes:
                # todo : NEED TO BE CHANGE TO NOTIFICATIONS
                self._likes.add(username_like)
                print("NOTIFICATION: {user_liked} Liked Your Post".format(user_liked=username_like))
            else:
                # todo : NEED TO BE CHANGE TO NOTIFICATIONS
                print("You've already liked")
        else:
            print("{username} Not Connected!".format(username=user.get_username()))


    # todo: DESCRIPTION
    def comment(self, user, comment_data):
        if user.is_connected:
            if comment_data is not None:
                self._comments.append((user.get_username(), comment_data))
                # todo : NEED TO BE CHANGE TO NOTIFICATIONS
                print("NOTIFICATION: {username} Comment Your Post".format(username=user.get_username()))

            else:
                print("Comment must contain at least one characters")

        else:
            "{username} Not Connected!".format(username=user.get_username())

    def __str__(self):
        pass


