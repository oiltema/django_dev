from django.urls import path

from .views import homepage, post_detail, sorted_by_tags, search_by_string, delete_comment, edit_comment

app_name = 'blog'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('post_detail/<slug:post_slug>/', post_detail, name='post_detail'),
    path('search/<slug:tag_slug>', sorted_by_tags, name='sorted_by_tags'),
    path('search/', search_by_string, name='search_by_string'),
    path('post_detail/delete/<int:comment_pk>/', delete_comment, name='delete_comment'),
    path('post_detail/edit/<int:comment_pk>/', edit_comment, name='edit_comment')
]