from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import  render
from django.shortcuts import get_object_or_404, render
from .models import Video_category, Video
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
            data.video_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()  # save data to table
            messages.success(request, "Your review has ben sent. Thank you for your interest.")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


def categories(request):
    return {
        'categories': Video_category.objects.all()
    }


def video(request):
    all_videos = Video.objects.all()
    context = {
        'all_videos': all_videos,
        }
    return render(request, 'content/video.html', context)


def category_list(request, category_slug=None):
    category = get_object_or_404(Video_category, slug=category_slug)
    videos = Video.objects.filter(category=category)
    return render(request, 'content/list.html', {'category': category, 'videos': videos})


def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    all_videos = Video.objects.all()

    context = {
        'video': video,
        'all_videos': all_videos,
        }

    return render(request, 'content/detail.html', context)
