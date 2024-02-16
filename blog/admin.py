from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'updated', 'status']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    ordering = ['status', 'publish']
    list_filter = ['status']

