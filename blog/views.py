from django.shortcuts import render, get_object_or_404
from .models import Article, Announcement
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from django.conf import settings


User = settings.AUTH_USER_MODEL

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 5

class UserArticleListView(ListView):
    model = Article
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=user).order_by('-date_posted')

def shared_images(request):
    context = {
        'images': Article.objects.all().order_by('-date_posted'),
        'title': 'Shared Images'
    }
    return render(request, 'blog/user_posts_images.html', context)

class ArticleDetailView(DetailView):
    model = Article

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content','video', 'image', 'add_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'content', 'video', 'image', 'add_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/'
    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class NoticeListView(ListView):
    model = Announcement
    template_name = 'blog/announcement.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'notices'
    ordering = ['-posted_date']
    paginate_by = 5


class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'add_video']

    def form_valid(self, form):
        form.instance.author = self.request.user
        super().form.save()
        return super().form_valid(form)

class NoticeDetailView(DetailView):
    model = Announcement


class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content', 'add_video']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False

class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    success_url = '/'
    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False




def searchBar(request):
    if request.method == "GET":
        query = request.GET.get('q')
        sub_btn = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'sub_btn': sub_btn,
                'title': 'Search Results'
            }
            return render(request, 'blog/search_results.html', context)

        else:
            return render(request, 'blog/search_results.html')
    else:
        return render(request, 'blog/home.html')

def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'blog/about.html', context)

