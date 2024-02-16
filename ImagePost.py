import matplotlib
from Posts import Posts


class ImagePost(Posts):
    __image_directory = None
    def __init__(self, user, *args):
        super().__init__(user, args)
        self.__image_directory = args
        print(self.__image_directory)

    def __str__(self):
        print("{username} posted a picture\n")

    # def display(self):
    #     if
    #     print("Shows picture"):