# SocialNetwork class - Singleton Design Pattern
from Users import Users
from error import SignUpError, SignInError, SignOutError


# todo: DESCRIPTION

class SocialNetwork:
    _instance = None

    # __new__ special method - creation of instances, cls is as self, **kwargs , keyboard words arguments
    # This method creating and returning a new instance of the class, only if there is no instance that exist
    # By that we make sure that only one instance of the SocialNetwork will be created.
    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)  # SocialNetwork single instance initialize
            cls._network_name = name  # network name initialize
            # User dictionary initialize
            # _user_data -> [ key = username : value = user(Object) ]
            cls._users_data = dict()
            print(f"The social network {name} was created!")
            return cls._instance
        else:
            print("Network Already Exists, Creation Failed!")
            return None

    # Special method being overridden, to print the data as required.
    # Printing each user data, implement in user class
    def __str__(self):
        social_network_data = f"{self._network_name} social network:\n"
        for username in self._users_data:
            social_network_data += str(self._users_data[username])  # Ensure string representation using casting
            social_network_data += "\n"  # Add a newline as a separator between users
        return social_network_data

    # Create new user to the social network
    def sign_up(self, username, password):
        # Exception:
        # 1. Arguments Validation
        if username is None or password is None:
            raise SignUpError
        # 2. Taken Username Validation
        elif username in self._users_data:
            raise SignUpError
        # 3. Password Validation
        elif 4 > len(password) or len(password) > 8:
            raise SignUpError
        # 4. Invalid Chars Validation (defined like this since I want to make sure the first Exception was checked)
        elif True:
            for char in username:
                if "'" in username or "(" in username or ")" in username or "," in username:
                    raise SignUpError

        # Sign Up - If all the Exceptions has Passed
        # Adding the user to the social network
        # _user_data -> [ ( key = username : value = (user(Object)) ) ]
        concrete_user = Users(username, password)
        self._users_data[username] = concrete_user
        return concrete_user

    # todo: DESCRIPTION
    def log_in(self, username, password):
        # Exceptions:
        # 1. Arguments Validation
        if username is None or password is None:
            raise SignInError
        # 2. Username Validation (check if username exist and user object exist)
        elif username not in self._users_data:
            raise SignInError
        # 3. Password Validation
        elif not self._users_data[username].check_password(password):
            raise SignInError
        # 4. User Connection Validation
        elif self._users_data[username].is_connected():
            raise SignInError('Username is already connected')

        # Log In
        else:
            user = self._users_data[username]
            user.connect()
            print(f"{user.username} connected")

    # todo: DESCRIPTION
    def log_out(self, username):
        # Exceptions
        # 1. Username Validation
        if username is None:
            raise SignOutError
        # 2. Username exist Validation
        elif username not in self._users_data:
            raise SignOutError
        # 3. Username Connected Validation
        elif not self._users_data[username].is_connected():
            raise SignOutError

        # Log Out
        else:
            self._users_data[username].disconnect()
            print(f"{username} disconnected")
