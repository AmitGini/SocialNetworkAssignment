# todo: add description
from CustomErrors import SubscriberNotFoundError


class Notifier:
    _subscribers = None

    def __init__(self):
        self._subscribers = set()

    # Adding subscribers to the list
    def add_subscriber(self, subscriber):
        try:
            if subscriber is None:  # Making sure subscriber is a valid user
                raise SubscriberNotFoundError
            self._subscribers.add(subscriber)  # Since it's a set there cant be duplicate values
        except (SubscriberNotFoundError, Exception) as e:
            print(e)

    # Removing subscribers to the list
    def remove_subscriber(self, subscriber):
        try:
            if subscriber is None:
                raise SubscriberNotFoundError
            self._subscribers.remove(subscriber)
        except (SubscriberNotFoundError, Exception) as e:
            print(e)

    # Sending notification to all the subscribers of a specific user (all users follow after user)
    def notify_all_subscriber(self, message):
        if message is not None and len(self._subscribers) > 0:
            try:
                for subscriber in self._subscribers:
                    subscriber.notification.update(message)
            except Exception as e:
                print(e)
                print("Notify subscribers Failed!")

    # Return the number of subscribers, this is the number of followers
    def get_num_subscriber(self):
        return len(self._subscribers)
