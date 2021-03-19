from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'header', 'date_posted']
    list_display_links = ['title']
    list_filter = ['date_posted']
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['post', 'date_commented']
    list_display_links = ['post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
