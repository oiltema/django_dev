from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()


@register.inclusion_tag('system/latest_post.html')
def latest_post(count=5):
    latest_posts = Post.published.all().order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def count_post():
    return Post.published.count()


@register.simple_tag
def most_comments_posts(count=5):
    return Post.published.annotate(total_comments=Count('post_comment')).order_by('-total_comments')[:count]