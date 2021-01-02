from django.db import models
from django.contrib.auth.models import User


class CategoryArt(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    avalaible = models.BooleanField(default=True)
    category = models.ForeignKey(CategoryArt, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="comments", related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='author_comm')
    body = models.TextField(max_length=400, verbose_name="your comment")
    date_post = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.post, self.author)


class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
