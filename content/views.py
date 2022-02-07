from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Video_category, Video


def categories(request):
    return {
        'categories': Video_category.objects.all()
    }


def video(request):
    # all_video = Video.objects.all()
    all_videos = Video.objects.all()
    context = {
        'all_videos': all_videos
        }
    return render(request, 'content/video.html', context)


def category_list(request, category_slug=None):
    category = get_object_or_404(Video_category, slug=category_slug)
    videos = Video.objects.filter(category=category)
    return render(request, 'content/list.html', {'category': category, 'videos': videos})


def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    context = {
        'video': video
        }

    return render(request, 'content/detail.html', context)
