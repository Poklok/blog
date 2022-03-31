from django.urls import path
from django.views.generic import DetailView

from main.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail')
]
