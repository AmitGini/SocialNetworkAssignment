
class Posts:
    _user = None
    _post_data = None
    _likes = None
    _comments = None

    def __init__(self, user, data):
        self._user = user
        self._post_data = data
        self._likes = dict()
        self._comments = list(tuple())

    def like(self, user):
        if user not in self._likes:
            self._likes[user.get_username()] = True
        else:
            pass

    def comment(self, user, comment_data):
        if comment_data is not None:
            self._comments.append((user.get_username(), comment_data))
    
    def __str__(self):
        pass


