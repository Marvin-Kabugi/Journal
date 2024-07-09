import threading
from django.core.mail import EmailMessage

class EmailThread(threading.Thread):
    def __init__(self, email) -> None:
        self.email = email
        super().__init__(self)

    def run(self):
        self.email.send()
class Utils:
    @staticmethod
    def send_email(data):
        email = EmailMessage()