from django.contrib import admin
from .models import Article, Announcement

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    #list_filter = ("status",)
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Announcement)
