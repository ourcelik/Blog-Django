from typing import ContextManager
from django.db import models
from django.db.models.fields import CharField, SlugField
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='PostImages', default='default.jpg')
    summary = RichTextField()
    content = RichTextField()
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    slug = models.SlugField(unique=True, editable=False, max_length=110)

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField(max_length=500)
    name = models.CharField(
        max_length=30, verbose_name='name', default='admin')
    date_commented = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, verbose_name=(
        "related-post"), on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-date_commented',)

    def __str__(self):
        return self.post.title + "_comment-"
