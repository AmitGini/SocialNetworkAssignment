from Posts import Posts


class TextPost(Posts):
    def __init__(self, user, *args):
        super().__init__(user, args)

    def __str__(self):
        print("{username} published a post:\n{post}".format(username=self._user, post=self._post_data))
