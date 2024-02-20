from rest_framework import serializers

from django.contrib.auth.models import User
from blog.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(view_name='post_detail', read_only=True, many=True, lookup_field='pk')
    url = serializers.HyperlinkedIdentityField(view_name='user_detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ['pk', 'url', 'username', 'posts']


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='post_detail', lookup_field='pk')
    author = serializers.CharField(source='author.username')
    post_comment = (serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment_detail', lookup_field='pk'))

    class Meta:
        model = Post
        fields = ['pk', 'url', 'author', 'title', 'content', 'updated', 'status', 'post_comment']


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment_detail', lookup_field='pk')
    author = serializers.CharField(source='author.username')
    post = serializers.CharField(source='post.title')

    class Meta:
        model = Comment
        fields = ['pk', 'url', 'author', 'post', 'text', 'updated']
        depth = 1

