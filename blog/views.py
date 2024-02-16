from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Post


def homepage(request):
    post = Post.published.all()
    context = {
        'post': post
    }
    return render(request, 'blog/homepage.html', context)


def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


def sorted_by_tags(request, tag_slug):
    post = Post.published.filter(tags__slug=tag_slug)
    context = {
        'post': post
    }
    return render(request, 'blog/homepage.html', context)


def search_by_string(request):
    post = Post.published.all()
    search = ''
    if request.method == 'POST':
        search = request.POST.get('search')
        post = post.filter(Q(title__icontains=search) | Q(content__icontains=search))
    context = {
        'post': post,
        'search': search
    }
    return render(request, 'blog/search_result.html', context)
