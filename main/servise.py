from django.core.mail import send_mail


def send(email):
    send_mail(
        'Вы подписались на рассылку',
        'Будет много спама',
        'poklokinde@gmail.com',
        [email]
    )
