from abc import ABC, abstractmethod


# Observer design pattern - Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass
