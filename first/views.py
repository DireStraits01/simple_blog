from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from django.db.models import Count
from django.views.generic.edit import UpdateView
from django.contrib import messages


def home(request):
    top_posts = Article.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:3]
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Article.objects.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Article.objects.all().order_by('date_create')[::-1]

    context = {'posts': posts, 'top_posts':top_posts}
    return render(request, 'first/home.html', context)
##############################Article############################################################

def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user.profile
            new_post.save()
            return HttpResponseRedirect('/')
    else:
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'first/add_article.html', context)

# article and comments page
def artical_page(request, id):
    post = get_object_or_404(Article, id=id)
   # dom = post.likes.get(profile_id=request.user.profile.id)
    comments = post.comments.filter()
    likes = post.likes.filter()
    if request.method == "POST":
        # if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user.profile
            new_comment.post = post
            new_comment.save()

            return HttpResponseRedirect(str(id))
    else:
        form = CommentForm()

        liked=False
        if  request.user.is_authenticated:
            if post.likes.filter(id=request.user.profile.id):
                liked=True
        context = {'post': post, 'comments': comments,
                   'form': form, 'likes':likes, 'liked':liked}
        return render(request, 'first/artical_page.html', context)

def update_post(request, id):
    post = Article.objects.get(id=id)
    author = post.author
    form = ArticleForm(instance=post)
    if post.author == request.user.profile:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('artical_page', args=[str(id)]))
    context = {'form':form, 'author':author}
    return render(request, 'first/update_post.html', context)






def likes_post(request, pk):
    post = get_object_or_404(Article, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.profile.id).exists():
        post.likes.remove(request.user.profile)
        liked=False
    else:
        post.likes.add(request.user.profile)
        liked=True
    return HttpResponseRedirect(reverse('artical_page', args=[str(pk)]))

