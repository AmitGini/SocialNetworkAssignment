from error.NotificationError import NotificationError


class Notifier:

    def __init__(self):
        self._watchers = set()

    def add_watcher(self, watcher):
        if watcher is not None:
            # No need to check if watcher already in the set, since there cant be duplicate values
            self._watchers.add(watcher)

    def remove_watcher(self, watcher):
        if watcher is not None:
            try:
                self._watchers.remove(watcher)

            except:
                raise NotificationError(watcher)

    def notify_watcher(self, watcher, message):
        if watcher is not self and message is not None:
            watcher.notification.update(message)
        else:
            raise NotificationError(watcher)

    def notify_all_watchers(self, message):
        if message is not None and len(self._watchers) > 0:
            for watcher in self._watchers:
                watcher.notification.update(message)
                print(self.username, message)