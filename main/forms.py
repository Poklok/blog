from django.forms import ModelForm
from django import forms

from main.models import Comment, SubscriptionToAlerts


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']


class SubscriptionToAlertsForm(forms.ModelForm):
    class Meta:
        model = SubscriptionToAlerts
        fields = ['email']
