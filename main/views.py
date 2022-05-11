from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from main.forms import SubscriptionToAlertsForm, CommentForm
from main.models import Post, SubscriptionToAlerts

from main.tasks import send_spam_mail

class PostListView(ListView):
    model = Post
    template_name = 'posts_list.html'
    context_object_name = 'posts'
    paginate_by = 3


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#     context_object_name = 'post'


class TestDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        return render(request, 'post_detail.html', {'post': post, 'comments': comments})


class AboutView(TemplateView):
    template_name = 'about.html'


class SubscriptionToAlertsView(CreateView):
    model = SubscriptionToAlerts
    form_class = SubscriptionToAlertsForm
    success_url = '/'
    template_name = 'email_subscription.html'

    def form_valid(self, form):
        form.save()
        send_spam_mail.delay(form.instance.email)
        return super().form_valid(form)
