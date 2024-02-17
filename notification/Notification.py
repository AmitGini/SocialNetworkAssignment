from notification.Watcher import Watcher


class Notification(Watcher):

    def __init__(self):
        super().__init__()
        self._notify_message = list()

    # Adding the notification message to the notification list
    def update(self, message):
        self._notify_message.append(message)

    # Iterate over the notification list and printing them from the first(oldest) to the last(newest)
    def display_notification(self, username):
        print(f"{username}'s notifications:\n")
        for message in self._notify_message:
            print(message)
