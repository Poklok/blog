from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from main.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts_list.html'
    context_object_name = 'posts'
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
