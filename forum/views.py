from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from forum.forms import AddNewPost, RegisterUserForm, LoginUserForm, AddCommentForm
from forum.models import Categories, Post, Comments


# Create your views here.

def main_page(request):
    return render(request, 'forum/main_page.html')

def new_post(request):
    data = {}

    if request.method == 'POST':
        form = AddNewPost(request.POST)
        data['form'] = form
        if form.is_valid():
            form.save()

            data['form'] = AddNewPost()
            return render(request, 'forum/new_post.html', data)


    else:
        data['form'] = AddNewPost()
    return render(request, 'forum/new_post.html', data)



cats = Categories.objects.all()

def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('forum:main_page')
    else:
        form = LoginUserForm()
    return render(request, 'forum/login_page.html', {'form':form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:login'))
    # return redirect('forum:main_page')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('forum:main_page')
    else:
        form = RegisterUserForm()

    return render (request, 'forum/register_page.html', {'form':form})

def cats_articles(request, slug_for_cats='all'):
    if slug_for_cats == 'all':
        articles = Post.objects.all()
    else:
        articles = Post.objects.filter(categories__slug_cat=slug_for_cats)
    data = {'articles':articles}

    return render(request, 'forum/articles_page.html', data)

def page_to_article(request, slug_for_art):
    aritcle = Post.objects.get(slug=slug_for_art)
    article_comments = Comments.objects.filter(post=aritcle.pk)

    if request.method == "POST" and request.user.username:
        form = AddCommentForm(request.POST)
        if form.is_valid():
            cm = form.save(commit=False)
            cm.author, cm.post = request.user, aritcle
            cm.save()
            return redirect('forum:page_to_article', slug_for_art)
    else:
        form = AddCommentForm()

    data ={'article':aritcle, 'form':form, 'article_comments':article_comments}

    return render(request, 'forum/single_article.html', data)

