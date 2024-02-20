from django.urls import path, include

from .views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('posts/create/', PostCreate.as_view(), name='post_create'),
    path('comments/', CommentList.as_view(), name='comments'),
    path('comments/<int:pk>', CommentDetail.as_view(), name='comment_detail'),
    path('comments/create', CommentCreate.as_view(), name='comment_create'),


]