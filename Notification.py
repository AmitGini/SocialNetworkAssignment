from Subscriber import Subscriber


# todo: add description

class Notification(Subscriber):

    def __init__(self):
        super().__init__()
        self._notify_message = list()

    # Adding the notification message to the notification list
    def update(self, message):
        try:
            self._notify_message.append(message)
        except Exception as e:
            print(e)
            print("Notification update/send Failed!")

    # Iterate over the notification list and printing them from the first(oldest) to the last(newest)
    def display_notification(self, username):
        try:
            print(f"{username}'s notifications:")
            for message in self._notify_message:
                print(message)
        except Exception as e:
            print(e)
            print("Display Notification Failed!")
