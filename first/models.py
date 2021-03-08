from django.db import models
from prof.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField

CATEGORY_TYPES = (
    ('Travel', 'Travel'),
    ('Cars', 'Cars'),
    ('It', 'It'),
    ('Sport', 'Sport'),
)
class Article(models.Model):
    title = models.CharField(max_length=255)
    # body = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_TYPES, verbose_name='category')
    body = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='author')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Profile)

    def total_likes(self):
       return self.likes.count()

    def __str__(self):
        return '%s-%s' % (self.title, self.category)


class Comment(models.Model):
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="comments", related_name='comments')
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name='author_comm')
    body = models.TextField(max_length=400, verbose_name="your comment")
    date_post = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s - %s' % (self.post, self.author, self.body)


