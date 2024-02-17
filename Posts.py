
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
                # todo : NEED TO BE CHANGE TO NOTIFICATIONS
                self._likes.add(user.username)
                print("NOTIFICATION: {user_liked} Liked Your Post".format(user_liked=user.username))
            else:
                # todo : NEED TO BE CHANGE TO NOTIFICATIONS
                print("You've already liked")
        else:
            print("{username} Not Connected!".format(username=user.username))


    # todo: DESCRIPTION
    def comment(self, user, comment_data):
        if user.is_connected:
            if comment_data is not None:
                self._comments.append((user.username, comment_data))
                # todo : NEED TO BE CHANGE TO NOTIFICATIONS
                print("NOTIFICATION: {username} Comment Your Post".format(username=user.username))

            else:
                print("Comment must contain at least one characters")

        else:
            "{username} Not Connected!".format(username=user.username)

    def __str__(self):
        pass


