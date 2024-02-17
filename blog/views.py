from django.shortcuts import render, redirect
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage

from .models import Post, Comment
from .forms import CommentForm


def homepage(request):
    post = Post.published.all()

    paginator = Paginator(post, 4)
    page_number = request.GET.get('page', 1)
    try:
        post = paginator.page(page_number)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'post': post,

    }
    return render(request, 'blog/homepage.html', context)


def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    comments = Comment.objects.filter(post__slug=post_slug)

    post_tags_list = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_list).exclude(slug=post_slug)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('same_tags', '-publish')[:4]

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.save(commit=False)
            cd.post = post
            cd.author = request.user
            cd.save()
            return redirect('blog:post_detail', post_slug)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'similar_posts': similar_posts,
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


def delete_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    post_slug = comment.post.slug
    comment.delete()
    return redirect('blog:post_detail', post_slug)


def edit_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    post = comment.post
    comments = Comment.objects.filter(post__pk=post.pk)
    if request.method == 'POST':
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post.slug)
    else:
        form = CommentForm(instance=comment)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/edit_comment.html', context)

