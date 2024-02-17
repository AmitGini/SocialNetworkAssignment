class NotificationError(Exception):
    def __init__(self,message="Notification Error"):
        super().__init__(message)
