from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy


def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Article.objects.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Article.objects.all()
    context = {'posts': posts}
    return render(request, 'first/home.html', context)


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect('/')
    else:
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'first/add_article.html', context)


def artical_page(request, id):
    post = get_object_or_404(Article, id=id)
    comments = post.comments.filter()

    if request.method == "POST":
        # if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

            return HttpResponseRedirect(str(id))
    else:
        form = CommentForm()
        context = {'post': post, 'comments': comments,
                   'form': form}
        return render(request, 'first/artical_page.html', context)
