from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class PostFactory:
    @staticmethod
    def create_post(user, post_type, *args):
        try:
            if post_type == "Text":
                return TextPost(user, *args)
            elif post_type == "Image":
                return ImagePost(user, *args)
            elif post_type == "Sale":
                return SalePost(user, *args)
        except:
            if post_type == "Text":
                raise ValueError("Invalid Input, Try publish_post(\"Text\",\"<Post Text>\"), Please try again")
            elif post_type == "Image":
                raise ValueError("Invalid Input, Try publish_post(\"Image\",\"<Image Directory>\"), Please try again")
            elif post_type == "Sale":
                raise ValueError("Invalid Input, Try publish_post(\"Sale\",\"<Item Description>\", <Price>, ,"
                                 "\"<Location>\"), Please try again")
            else:
                raise ValueError("Invalid Type, Try again")
