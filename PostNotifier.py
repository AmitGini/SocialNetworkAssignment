from NotificationService import NotificationService


# Observer - Design pattern
# Concrete NotificationService implementation of NotificationService
# (Concrete NotificationService/ Concrete Sender)
class PostNotifier(NotificationService):
    def send_new_post_notification(self, username):
        message = f"{username} has a new post"
        self.notify(message)
