from django.contrib import admin
from .models import Category, Post, Author, Comment, PostView


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
    list_display = ['user']


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ['user']