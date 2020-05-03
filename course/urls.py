from django.urls import path
from . import views

urlpatterns = [
    path('', views.eNepal, name='eNepal'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('secondary/', views.secondary, name='secondary'),
    path('contact/', views.contact, name='contact'),
    path('primary/', views.primary, name='primary'),
    path('lsecondary/', views.lowerSecondary, name='lower-secondary'),
    path('secondary/science/', views.secScience, name='sec-science'),
    path('secondary/math/', views.secMath, name='sec-math'),
    path('secondary/cs/', views.secComputer, name='sec-computer'),
    path('primary/science/', views.priScience, name='pri-science'),

]
