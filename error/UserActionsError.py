class FollowingError(Exception):
    """
        Raised when an invalid input is entered or invalid argument passed
        when trying to follow or unfollow user that:
        1. User Not Exist
        2. User already been Followed
        3. User already been Unfollowed

        Attributes:

            type -- 1/2/3
            message -- explanation of the error


    """
    def __init__(self, follow_unfollow_NotExist):
        message = "User "
        switch (follow_unfollow_NotExist):


        super().__init__(message)