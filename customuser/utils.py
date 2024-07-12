import threading
from django.core.mail import EmailMessage
from datetime import timedelta, datetime
from django.conf import settings
import jwt

class EmailThread(threading.Thread):
    def __init__(self, email) -> None:
        self.email = email
        super().__init__()

    def run(self):
        self.email.send()


class Utils:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_message'], to=[data['email']])
        email.content_subtype = 'html'
        EmailThread(email).start()

    @staticmethod
    def generate_confirmation_token(user):
        payload = {
            'user_id': user.id,
            'exp': datetime.now() + timedelta(hours=1),
            'iat': datetime.now(),
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token

