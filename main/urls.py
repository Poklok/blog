from django.urls import path
from django.views.generic import DetailView

from main.views import PostListView, PostDetailView, AboutView, SubscriptionToAlertsView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('about', AboutView.as_view(), name='about'),
    path('email_sub', SubscriptionToAlertsView.as_view(), name='email')
]
