from abc import ABC

from CustomErrors import SubscriberNotFoundError


# Observer Design Pattern - abstract (Publisher/Sender)
# abstract class that responsible to add or remove from the subscribers list of specific user
#           and also responsible to notify the subscribers of specific user
class NotificationService(ABC):
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
    def notify(self, message):
        if message is not None and len(self._subscribers) > 0:
            try:
                for subscriber in self._subscribers:
                    subscriber.update(message)
            except Exception as e:
                print(e)
                print("Notify subscribers Failed!")

    # Return the number of subscribers, this is the number of followers
    def get_num_subscriber(self):
        return len(self._subscribers)
