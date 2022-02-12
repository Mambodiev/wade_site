from django.contrib import admin
from .models import Category, Post, PostView, Author, Comment, Like


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug',
                    'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user']
   

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'approved', 'timestamp']
    list_editable = ['approved',]


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user']