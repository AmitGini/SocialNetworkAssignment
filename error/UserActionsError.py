# General Errors
NOT_EXIST = "Error! User Not Exist"

# Following Error
FOLLOW = "Already been Followed"
NOT_FOLLOWED = "Following never occur Error, Cant Unfollow"
FOLLOW_SELF = "Error! User Cannot Follow it Self"
UNFOLLOW_SELF = "Error! User Cannot UnFollow it Self"
# Posts Error
RE_LIKE = "Error! Already Liked"
EMPTY_COMMENT = "Error! Trying to comment, to Unknown Post"


class UserActionsError(Exception):
    """
        Raised when an invalid input is entered or invalid argument passed
        when trying to follow or unfollow user that:
        1. User Not Exist
        2. User already been Followed
        3. User never been followed/already been Unfollowed
        4. User trying Like Unknown post
        5. User trying Comment Unknown post

        Attributes:

            type -- 1/2/3
            message -- explanation of the error


    """

    def __init__(self, error_type):
        # General Errors
        message = ""
        if error_type == "NotExist":
            message = NOT_EXIST

        # Follow Error
        elif error_type == "FollowedAlready":
            message = FOLLOW
        elif error_type == "FollowSelf":
            message = FOLLOW_SELF
        elif error_type == "NotFollowed":
            message = NOT_FOLLOWED
        elif error_type == "UnfollowSelf":
            message = UNFOLLOW_SELF
        elif error_type == "EmptyComment":
            message = EMPTY_COMMENT
        elif error_type == "RepeatLike":
            message = RE_LIKE
        super().__init__(message)
