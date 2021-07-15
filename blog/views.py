from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def about(request):
    return render(request, 'blog/about.html')


class PostListViews(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'postss'
    ordering = ['-date'] # newest to oldest
    paginate_by = 3


class UserPostListViews(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'postss'
    ordering = ['-date']  # newest to oldest
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


class PostDetailViews(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'


class PostCreateViews(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # takes a default template form_post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateViews(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'
    success_message = '%(title)s Post Updated!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False


class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    success_url = '/'
    success_message = '%(title)s Post Deleted!'

    def test_func(self):
        if self.request.author == self.get_object().author:
            return True
        return False

    template_name = 'blog/delete-post.html'
