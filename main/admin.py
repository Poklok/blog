from django.contrib import admin

# Register your models here.
from main.models import Post, Comment, SubscriptionToAlerts

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SubscriptionToAlerts)
