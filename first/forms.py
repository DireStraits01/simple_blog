from django.forms import ModelForm
from .models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('category', 'title', 'image', 'body')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
