from CustomErrors import InvalidPostTypeError, InvalidPostDataError
from PostImage import PostImage
from PostSale import PostSale
from PostText import PostText


# Factory Design Pattern
# Post factory, static method, responsible to create the post according to the type
class PostFactory:
    @staticmethod
    def create_post(user, post_type, *args):
        try:
            if args is None or len(args) < 1:  # Exceptions: Validation arguments, notifier, type, args
                raise InvalidPostDataError
            # Posts Creation By Type
            elif post_type == "Text":  # Text
                return PostText(user, args[0])  # Creating Text Post
            elif post_type == "Image":  # Image
                return PostImage(user, args[0])  # Creating Image Post
            elif post_type == "Sale":  # Sale
                return PostSale(user, *args)  # Creating Sale Post
            else:
                raise InvalidPostTypeError
        except (InvalidPostTypeError, InvalidPostDataError, Exception) as e:
            print(e)
