from CustomErrors import InvalidPostTypeError, InvalidPostDataError, SalePostCreationError
from PostImage import PostImage
from PostSale import PostSale
from PostText import PostText


# Factory Design Pattern
# Post factory, static method, responsible to create the post according to the type
# Constant indexes to prevent unknown number in the code
PRODUCT_INDEX = 0  # Index in the data list of the sale post
PRICE_INDEX = 1  # Index in the data list of the sale post
LOCATION_INDEX = 2  # Index in the data list of the sale post
class PostFactory:
    # Posts Creation By Type
    @staticmethod
    def create_post(user, post_type, *args):
        try:
            if args is None or len(args) < 1:  # Exceptions: Validation arguments, notifier, type, args
                raise InvalidPostDataError
            elif post_type == "Text":  # Text
                return PostText(user, args[0])  # Creating Text Post
            elif post_type == "Image":  # Image
                return PostImage(user, args[0])  # Creating Image Post
            elif post_type == "Sale":  # Sale
                try:  # Validation of proper arguments for sale post
                    if len(args[PRODUCT_INDEX]) < 1 or args[PRICE_INDEX] < 1 or len(args[LOCATION_INDEX]) < 1:
                        raise SalePostCreationError
                    return PostSale(user, args[PRODUCT_INDEX], args[PRICE_INDEX], args[LOCATION_INDEX])  # Creating Sale Post
                except (SalePostCreationError, Exception) as e:
                    print(e)
            else:
                raise InvalidPostTypeError
        except (InvalidPostTypeError, InvalidPostDataError, Exception) as e:
            print(e)
