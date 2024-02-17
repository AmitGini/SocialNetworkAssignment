import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from Posts import Posts


# todo: DESCRIPTION
class ImagePost(Posts):

    def __init__(self, user, args):
        super().__init__(user, args)

    # Special method being overridden, to print the data as required.
    def __str__(self):
        return "{username} posted a picture\n".format(username=self.publisher_username)

    # todo: DESCRIPTION
    def display(self):
        # Load the image file
        image_path = self._post_data
        img = mpimg.imread(image_path)

        # Display the image
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        print("Shows picture")
