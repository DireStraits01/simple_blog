from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def home(request):
    posts = Article.objects.filter(avalaible=True)
    context = {'posts': posts}
    return render(request, 'first/home.html', context)


@login_required
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            form = ArticleForm()
            context = {'form': form}
            return render(request, 'first/add_article.html', context)
    else:
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'first/add_article.html', context)


def artical_page(request, id):
    post = get_object_or_404(Article, id=id, avalaible=True)
    comments = post.comments.filter()

    if request.method == "POST":
        # if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            form = CommentForm()

    else:
        form = CommentForm()
    context = {'post': post, 'comments': comments,
               'form': form}
    return render(request, 'first/artical_page.html', context)
