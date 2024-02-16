from Posts import Posts


# todo: DESCRIPTION
class TextPost(Posts):
    def __init__(self, user, args):
        super().__init__(user, args)

    # Special method being overridden, to print the data as required.
    def __str__(self):
        return "{username} published a post:\n\"{post}\"\n".format(username=self._user.get_username(), post=self._post_data)
