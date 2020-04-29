from django.urls import path
from . import views
from .views import (ArticleListView, ArticleDetailView, ArticleCreateView,
                    ArticleUpdateView, ArticleDeleteView, UserArticleListView,
                    NoticeCreateView, NoticeListView, NoticeDetailView,
                    NoticeUpdateView, NoticeDeleteView)


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-home'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('search/', views.searchBar, name='searchBar'),
    path('announcements/', NoticeListView.as_view(), name='announcements'),
    path('article/new/', ArticleCreateView.as_view(template_name='blog/article_form.html'), name='new-article'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update')
]
