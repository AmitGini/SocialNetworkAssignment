from error.CustomError import CustomError


class NotConnectionError(CustomError):
    def __init__(self, message = "User is Not Connected, Try Log in"):
        super().__init__(message)