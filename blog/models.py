from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images')
    video = models.FileField(blank=True, null=True, upload_to='videos')
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    add_video = models.FileField(upload_to='videos/', null=True, verbose_name="Add Video")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})


