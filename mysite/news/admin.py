from django.contrib import admin

from .models import *


class NewsConfig(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class CategoryConfig(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class LikesConfig(admin.ModelAdmin):
    list_display = ('post', 'likes')
    list_display_links = ('post',)


class CommentsConfig(admin.ModelAdmin):
    list_display = ('post', 'comment')
    list_display_links = ('post',)
    search_fields = ('post', 'comment')


admin.site.register(News, NewsConfig)
admin.site.register(Category, CategoryConfig)
admin.site.register(Likes, LikesConfig)
admin.site.register(Comments, CommentsConfig)
