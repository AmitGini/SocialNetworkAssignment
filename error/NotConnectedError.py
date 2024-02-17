class NotConnectedError(Exception):
    """
        Raised when an invalid input is entered or invalid argument passed

        Attributes:

            message -- explanation of the error

    """
    def __init__(self, message="User is Not Connected, Try Log in"):
        super().__init__(message)