from django.urls import path

from .views import homepage, post_detail, sorted_by_tags, search_by_string

app_name = 'blog'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('post_detail/<slug:post_slug>/', post_detail, name='post_detail'),
    path('search/<slug:tag_slug>', sorted_by_tags, name='sorted_by_tags'),
    path('search/', search_by_string, name='search_by_string'),
]