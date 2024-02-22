from Post import Post


# Factory Design Pattern
# Text Post implements Post, contain textual data only
class PostText(Post):
    def __init__(self, author, text):
        super().__init__(author=author, data=text)  # Initial the post
        print(self)  # Printing post after creation

    # Special method being overridden, creating custom String for printing
    def __str__(self):
        return f'{self._author.username} published a post:\n\"{self._post_data}\"\n'
