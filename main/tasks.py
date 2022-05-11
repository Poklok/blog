from Blog.celery import app
from main.servise import send


@app.task
def send_spam_mail(email):
    send(email)
