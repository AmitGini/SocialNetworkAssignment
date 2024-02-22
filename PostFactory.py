from CustomErrors import InvalidPostTypeError, InvalidPostDataError
from post.ImagePost import ImagePost
from post.SalePost import SalePost
from post.TextPost import TextPost


# todo: DESCRIPTION
class PostFactory:
    @staticmethod
    def create_post(user, post_type, *args):
        try:
            if args is None or len(args) < 1:  # Exceptions: Validation arguments, notifier, type, args
                raise InvalidPostDataError
            # Posts Creation By Type
            elif post_type == "Text":  # Text
                return TextPost(user, args[0])  # Creating Text Post
            elif post_type == "Image":  # Image
                return ImagePost(user, args[0])  # Creating Image Post
            elif post_type == "Sale":  # Sale
                return SalePost(user, *args)  # Creating Sale Post
            else:
                raise InvalidPostTypeError
        except (InvalidPostTypeError, InvalidPostDataError, Exception) as e:
            print(e)
