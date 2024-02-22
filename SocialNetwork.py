from CustomErrors import SignUpError, SignInError, SignOutError
from Users import Users


# SocialNetwork class - Singleton Design Pattern
# representing a social network that can be signed up new user, sign in or sign out, and saving users information (dict)
class SocialNetwork:
    _instance = None  # represent the single instance of the social network
    _network_name = None  # the name of the network the given in the first creation
    _user_data = None  # dictionary holding the username as a key and Users object as value

    # __new__ special method - creation of instances, cls is as self, **kwargs , keyboard words arguments
    # This method creating and returning a new instance of the class, only if there is no instance that exist
    # By that we make sure that only one instance of the SocialNetwork will be created.
    def __new__(cls, name):
        if cls._instance is None:
            cls._network_name = name  # network name initialize
            cls._users_data = dict()  # _user_data -> [ key = username : value = notifier(Object) ]
            print(f"The social network {name} was created!")
        else:
            print("Network Already Exists, Creation Failed!")
        cls._instance = super(SocialNetwork, cls).__new__(cls)  # SocialNetwork single instance initialize
        return cls._instance

    # Printing each notifier data, implement in notifier class
    def __str__(self):
        social_network_data = f"{self._network_name} social network:"  # Initial Custom String
        for username in self._users_data:  # Iterate on the notifier data dictionary
            social_network_data += "\n"  # Add a newline as a separator between users
            social_network_data += str(self._users_data[username])  # Building custom String for printing
        return social_network_data

    # Create new notifier to the social network, connected by default
    def sign_up(self, username, password):
        try:
            if username is None or password is None:  # 1. Exceptions: Arguments Validation
                raise SignUpError("Username or password cannot be None.")
            elif username in self._users_data:  # 2. Exceptions: Taken Username Validation
                raise SignUpError("Username is already taken.")
            elif 4 > len(password) or len(password) > 8:  # 3. Exceptions: Password Validation
                raise SignUpError("Password must be between 4 and 8 characters.")
            elif "'" in username or "(" in username or ")" in username or "," in username:  # 4. Exceptions: Invalid Chars
                raise SignUpError("Username contains invalid characters.")
            concrete_user = Users(username, password)  # Creating User Object
            self._users_data[username] = concrete_user  # Adding User Object to the dictionary data
            return concrete_user  # Return the notifier Object
        except (SignUpError, Exception) as e:
            print(e)

    # Log in, responsible for information validation and entering the notifier account - access for notifier actions
    def log_in(self, username, password):
        try:
            if username is None or password is None:  # 1. Exceptions: Arguments Validation
                raise SignInError("Username or password cannot be None.")
            elif username not in self._users_data:  # 2. Exceptions: Username Validation
                raise SignInError("Username does not exist.")
            elif self._users_data[username].is_connected():  # 3. Exceptions: User Connection Validation
                raise SignInError("User is already connected.")
            elif self._users_data[username].connect(password):  # Changing User Status to connected, Password validation happened in the connect method and return if succeed
                print(f"{username} connected")
        except (SignInError, Exception) as e:
            print(e)

    # Log out, responsible for validate the username and disconnect the notifier account - prevent notifier actions
    def log_out(self, username):
        try:
            if username is None:  # 1. Exceptions: Username Validation
                raise SignOutError("Username cannot be None.")
            elif username not in self._users_data:  # 2. Exceptions: Username exist Validation
                raise SignOutError("Username does not exist.")
            elif not self._users_data[username].is_connected():  # 3. Exceptions: Username Connected Validation
                raise SignOutError("User is not connected, SignOut Failed.")
            elif self._users_data[username].disconnect(username):  # Changing User Status to Disconnected
                print(f"{username} disconnected")
        except (SignOutError, Exception) as e:
            print(e)
