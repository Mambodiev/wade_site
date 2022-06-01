from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from .models import Category, Post, PostView, Like
from .forms import CommentForm, Comment


def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()  # create relation with model
            data.content = form.cleaned_data['content']
            data.ip = request.META.get('REMOTE_ADDR')
            data.post_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()  # save data to table
            messages.success(request, "Your review has ben sent. Thank you for your interest.")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)

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
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)


    context = {
        'post': post,
        }

    return render(request, 'blog/posts/detail.html', context)


def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)


def page_not_found_view(request, exception):
    return render(request, 'blog/not-found.html')