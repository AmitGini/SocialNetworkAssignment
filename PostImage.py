import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from Post import Post


#                           Structure Design pattern
# Image post implements post, contain path directory and show the image
class PostImage(Post):

    def __init__(self, author, image_url):
        super().__init__(author=author)
        self.__image_url = image_url
        print(self)

    # Special method being overridden, creating custom String for printing
    def __str__(self):
        return f"{self._author.username} posted a picture\n"

    # Responsible for showing the picture of a given path directory
    def display(self):
        try:
            image_path = self.__image_url  # Load the image file
            img = mpimg.imread(image_path)  # Load the image file
            plt.imshow(img)  # Display the image
            plt.axis('off')  # Display the image - Removing scales
            plt.show()  # Display the image
            print("Shows picture")  # Printing display notification
        except Exception as e:
            print(e)
