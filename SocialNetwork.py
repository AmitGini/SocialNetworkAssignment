# SocialNetwork class - Singleton Design Pattern
from Users import Users


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
            # _user_data -> [ ( key = username : value = (user(Object)) ) ]
            cls._users_data = dict()
            print("The social network {network_name} was created!".format(network_name=name))
            return cls._instance
        else:
            print("Network Already Exists, Creation Failed!")
            return None

    # Create new user to the social network
    def sign_up(self, username, password):
        # Checking if there is no other user with the same username
        if username not in self._users_data:
            pass_length = len(password)

            if 4 <= pass_length <= 8:
                # Adding the user to the social network
                # _user_data -> [ ( key = username : value = (user(Object)) ) ]
                concrete_user = Users(username, password)
                self._users_data[username] = concrete_user
                return concrete_user
            else:
                print("Invalid Password, Please try again!")
                return None
        else:
            print("{} is in Use, Please try Different Username!".format(username))
            return None

    def log_in(self, username, password):
        # Check if there is such username id the data
        if self._users_data.get(username) is not None:
            # Username exist, we retrieve its data and check if the password is correct
            user = self._users_data.get(username)
            # Password Check
            if user.check_password(password):
                # Check if the user is already connected
                if not user.is_connected():
                    print("{} connected!".format(username))  # connect successfully notification
                    return  # return the user object

                # Already connected Notification
                else:
                    print("{} User Already Connected!".format(username))

        # If the username or the password are wrong it will print the following line
        print("{} Invalid Username or Password, Please try again Or Sign up".format(username))
        return None

    def log_out(self, username):
        # Check if there is such username id the data
        if self._users_data.get(username) is not None:
            user = self._users_data.get(username)
            if user.is_connected():
                user.disconnect()
                print("{} disconnected!".format(username))
            else:
                print("User Already Disconnected!")
        else:
            print("{} Username was not found!".format(username))
