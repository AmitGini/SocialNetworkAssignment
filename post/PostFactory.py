from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


# todo: DESCRIPTION
class PostFactory:
    @staticmethod
    def create_post(user, post_type, *args):
        # Validation arguments, user, type, args
        if not user:
            raise ValueError("User is required to publish a post.")

        # Further validation depending on the post type
        if post_type == "Text":
            if len(args) < 1:  # Assuming the first argument is the post text
                raise ValueError("Missing text for the TextPost.")

            else: return TextPost(user, args[0])  # Creating Text Post

        elif post_type == "Image":
            if len(args) < 1:  # Assuming the first argument is the image path
                raise ValueError("Missing image path for the ImagePost.")

            else: return ImagePost(user, args[0])  # Creating Image Post

        elif post_type == "Sale":
            if len(args) < 3:  # Assuming the arguments are item description, price, and location
                raise ValueError("Missing data for the SalePost. Required: item description, price, and location.")

            else: return SalePost(user, args)  # Creating Sale Post

        else:
            raise ValueError("Invalid post type. Available types are: Text, Image, Sale.")


