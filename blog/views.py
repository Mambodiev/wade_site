from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .models import Category, Post


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def home(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
        }

    return render(request, 'blog/home.html', context)


def post_all(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/posts/category.html', {'category': category, 'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/posts/detail.html', {'post': post})