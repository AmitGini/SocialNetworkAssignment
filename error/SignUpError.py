class SignUpError(Exception):
    def __init__(self):
        self.message = ("Invalid Username or Password, Please try again\nUsername cant contain ,)'( \nPassword must be "
                        "at least 4 characters long and at most 8 characters long\n")
        super().__init__(self.message)