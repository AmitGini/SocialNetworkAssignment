class SignUpError(Exception):
    def __init__(self, message):
        if message is not None:
            if len(message) > 0:
                self.message = message
        self.message = "Invalid Username or Password, Please try again or Sign up!"
        super().__init__(self.message)