from django.urls import path
from . import views

urlpatterns = [
    path('', views.eNepal, name='eNepal'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('secondary/', views.grade1, name='secondary'),
    path('contact/', views.contact, name='contact')
]
