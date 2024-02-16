from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse

from taggit.managers import TaggableManager


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISH)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISH = 'PB', 'Опубликовано'

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name='Автор')

    title = models.CharField(max_length=155, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='Слаг')
    content = models.TextField(max_length=2000, verbose_name='Контент')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано')

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')

    objects = models.Manager()
    published = PublishManager()
    tags = TaggableManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return f'{self.title}, {self.author}, {self.created}, {self.status}'

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'post_slug': self.slug})


