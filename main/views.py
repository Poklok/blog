from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from main.forms import SubscriptionToAlertsForm
from main.models import Post, SubscriptionToAlerts


class PostListView(ListView):
    model = Post
    template_name = 'posts_list.html'
    context_object_name = 'posts'
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class AboutView(TemplateView):
    template_name = 'about.html'


class SubscriptionToAlertsView(CreateView):
    model = SubscriptionToAlerts
    form_class = SubscriptionToAlertsForm
    success_url = '/'
    template_name = 'email_subscription.html'
