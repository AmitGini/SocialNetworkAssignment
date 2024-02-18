class SignOutError(Exception):
    def __init__(self, message):
        if message is not None:
            if len(message) > 0:
                self.message = message
        self.message = "Error! Invalid Username or Username is already Signed out"
        super().__init__(self.message)