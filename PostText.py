from Posts import Posts


# todo: DESCRIPTION
class PostText(Posts):
    def __init__(self, user, args):
        super().__init__(user, args)
        print(self)

    # Special method being overridden, creating custom String for printing
    def __str__(self):
        return f'{self._user.username} published a post:\n\"{self._post_data}\"\n'
