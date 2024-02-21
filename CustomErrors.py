#  System Network

class SignUpError(Exception):
    def __init__(self, message="Sign up failed"):
        super().__init__(message)


class SignInError(Exception):
    def __init__(self, message="Sign in failed"):
        super().__init__(message)


class SignOutError(Exception):
    def __init__(self, message="Sign out failed"):
        super().__init__(message)


class WrongPassword(PermissionError):
    def __init__(self):
        message = "Wrong password! Please try!"
        super().__init__(message)


class WrongUsername(PermissionError):
    def __init__(self):
        message = "Wrong Username! Please try!"
        super().__init__(message)


#  User and Posts Errors

class NotConnectedError(PermissionError):
    def __init__(self, username=None):
        message = f"{username} Not connected! Please try Log In first." if username else "Not connected! Please try Log In first."
        super().__init__(message)


class UserNotDefinedError(Exception):
    def __init__(self):
        message = "The given User does Not Exist!"
        super().__init__(message)


class UserSubscribeItSelf(Exception):
    def __init__(self):
        message = "Follow/Unfollow yourself is an illegal Action!"
        super().__init__(message)


class AlreadyLikedError(Exception):
    def __init__(self, username=None):
        message = f"{username} has already liked this post." if username else "This post has already been liked by the user."
        super().__init__(message)


class AlreadyFollowingError(Exception):
    def __init__(self, username=None):
        message = f"Can't follow {username}; already following." if username else "Already following this user."
        super().__init__(message)


class NotFollowingError(Exception):
    def __init__(self, username=None):
        message = f"Can't unfollow {username}; you are not following them." if username else "You are not following this user."
        super().__init__(message)


class InvalidPostTypeError(TypeError):
    def __init__(self, message="Invalid post type. Available types are: Text, Image, Sale."):
        super().__init__(message)


class InvalidPostDataError(TypeError):
    def __init__(self,
                 message="Invalid post data, must contain at least 1 Characters"):
        super().__init__(message)


class SalePostCreationError(TypeError):
    def __init__(self,
                 message="Invalid post data, Sale - Product description at least 1 char, price - only positive numbers, location, at least 1 chars"):
        super().__init__(message)


class ProductSoldError(TypeError):
    def __init__(self,
                 message="Product already been Sold!"):
        super().__init__(message)


class InvalidDiscountError(TypeError):
    def __init__(self,
                 message="Invalid discount rate, Must be between 1-100"):
        super().__init__(message)


class EmptyCommentError(ValueError):
    def __init__(self, message="Empty Comment"):
        super().__init__(message)


class SubscriberNotFoundError(ValueError):
    def __init__(self, message="Subscriber is Not defined"):
        super().__init__(message)


class InvalidSubscriberError(ValueError):
    def __init__(self, message="Invalid subscriber action performed"):
        super().__init__(message)
