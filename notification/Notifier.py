class Notifier:

    def __init__(self):
        self._watchers = list()

    def add_watcher(self, watcher):
        if watcher is not None:
            self._watchers.append(watcher)

    def remove_watcher(self, watcher):
        if watcher is not None:
            try:
                self._watchers.remove(watcher)

            except:
                raise ValueError("Error! {watcher} was not following".format(wacher=watcher.username))

    def notify_watchers(self, message):
        if message is not None:
            for watcher in self._watchers:
                watcher.update(message)
