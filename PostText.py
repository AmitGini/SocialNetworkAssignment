from Post import Post


# Structure Design pattern
# Text Post implements Post, contain textual data only
class PostText(Post):
    def __init__(self, author, text):
        super().__init__(author=author)  # Initial the post
        self.__post_text = text
        print(self)  # Printing post after creation

    # Special method being overridden, creating custom String for printing
    def __str__(self):
        return f'{self._author.username} published a post:\n\"{self.__post_text}\"\n'
