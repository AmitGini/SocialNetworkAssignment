from NotificationService import NotificationService

# Observer - Design pattern
# Concrete NotificationService implementation of NotificationService
# (Concrete NotificationService/ Concrete Sender)
class PostPublisher(NotificationService):
    def send_new_post_notification(self, username):
        message = f"{username} has a new post"
        print(message)
        self.notify(message)