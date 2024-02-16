from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(max_length=1500, verbose_name='Статья')
    rating = models.IntegerField()
    author = models.CharField(max_length=255, verbose_name='Автор')

