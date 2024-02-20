import datetime
from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    class PrintedPost(models.TextChoices):
        PRINTED = "PR", "Printed"
        DRAFT = "DR", "Draft"
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(max_length=1500, verbose_name='Статья')
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=255, verbose_name='Автор')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=PrintedPost.choices,
                              default=PrintedPost.DRAFT)
    slug = models.SlugField(max_length=255, unique=True)
    categories = models.ForeignKey('Categories', on_delete=models.DO_NOTHING,)


    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=255)
    slug_cat = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000)
    def __str__(self):
        return f"{self.author} {self.comment[:7]}"

