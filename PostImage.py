import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from Posts import Posts


# todo: DESCRIPTION
class PostImage(Posts):

    def __init__(self, user, args):
        super().__init__(user, args)
        print(self)

    # Special method being overridden, creating custom String for printing
    def __str__(self):
        return f"{self._user.username} posted a picture\n"

    # Responsible for showing the picture of a given path directory
    def display(self):
        try:
            image_path = self._post_data  # Load the image file
            img = mpimg.imread(image_path)  # Load the image file
            plt.imshow(img)  # Display the image
            plt.axis('off')  # Display the image - Removing scales
            plt.show()  # Display the image
            print("Shows picture")  # Printing display notification
        except Exception as e:
            print(e)