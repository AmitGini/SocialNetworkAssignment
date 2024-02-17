from Watcher import Watcher


class Notification(Watcher):

    def __init_(self, user):
        self.__user = user
        self.__notify_message = list()

    # Adding the notification message to the notification list
    def update(self, message):
        self.__notify_message.append(message)

    # Iterate over the notification list and printing them from the first(oldest) to the last(newest)
    def display_notification(self):
        print("{username}'s notifications:\n".format(username=self.__user.username))
        for message in self.__notify_message:
            print(message)
