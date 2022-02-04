from audioop import reverse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render, reverse
from .models import Category, Post, PostView, PostLike
from .forms import CommentForm


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


def post(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list,4)
    page_request_var = 'page'
    page = request.GET.get('page_request_var')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        }
    return render(request, 'blog/posts/blog.html', context)


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/posts/category.html', {'category': category, 'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        PostView.objects.get_or_create(user=request.user, post=post)



    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if request.user.is_active:

                form.instance.user = request.user
                form.instance.post = post
                form.save()
            return redirect(reverse('post_detail', kwargs={
                'id':post.pk            
            }))
    context = {
        'form':form,
        'post': post
        }

    return render(request, 'blog/posts/detail.html', context)


def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        like_qs = PostLike.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    if request.user.is_active:

        PostLike.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)