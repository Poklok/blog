from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/posts',)

    def __str__(self):
        return self.title
