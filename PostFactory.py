from enum import Enum
from PostImage import PostImage
from PostSale import PostSale
from PostText import PostText


# Factory Design Pattern
class PostType(Enum):
    TEXT = "Text"  # Representation of text post
    IMAGE = "Image"  # Representation of image post
    SALE = "Sale"  # Representation of sale post


# Post factory, static method, responsible to create the post according to the type
# Constant indexes to prevent unknown number in the code
PRODUCT_INDEX = 0  # Index in the data list of the sale post
PRICE_INDEX = 1  # Index in the data list of the sale post
LOCATION_INDEX = 2  # Index in the data list of the sale post


class PostFactory:
    # Posts Creation By Type
    @staticmethod
    def create_post(user, post_type, *args):
        if args is None or len(args) < 1:  # Exceptions: Validation arguments, notifier, type, args
            return None
        elif PostType[post_type.upper()] == PostType.TEXT:  # Text
            return PostText(user, args[0])  # Creating Text Post
        elif PostType[post_type.upper()] == PostType.IMAGE:  # Image
            return PostImage(user, args[0])  # Creating Image Post
        elif PostType[post_type.upper()] == PostType.SALE:  # Sale
            if len(args[PRODUCT_INDEX]) < 1 or args[PRICE_INDEX] < 1 or len(args[LOCATION_INDEX]) < 1:  # Argument Validations
                return None
            return PostSale(user, args[PRODUCT_INDEX], args[PRICE_INDEX], args[LOCATION_INDEX])  # Creating Sale Post
        else:
            return None
