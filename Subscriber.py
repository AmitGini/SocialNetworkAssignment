from abc import ABC, abstractmethod


# Observer design pattern - Interface represent an observer
# abstract class - representing subscriber that can be notified using update when
#                   other user published a post and he's part of its subscribers list
#                   OR user comment or liked my post I will be notified using update
class Subscriber(ABC):
    @abstractmethod
    def update(self, message):
        pass
