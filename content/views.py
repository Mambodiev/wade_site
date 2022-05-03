from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import  render
from django.shortcuts import get_object_or_404, render
from .models import Videocategory, Video, VideoView
from .forms import CommentForm, Comment
from django.views.generic import ListView

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
        'categories': Videocategory.objects.all()
    }

class HomeView(ListView):
    template_name = 'content/video.html'
    model = Videocategory
    context_object_name = 'all_categs'

    def get_queryset(self):
       return Videocategory.objects.all()

    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context['latest_videos'] = Video.objects.order_by('-date_posted')[0:3] 
        return context

# def video(request):
#     all_videos = Video.objects.all()
#     context = {
#         'all_videos': all_videos,
#         }
#     return render(request, 'content/video.html', context)


def category_list(request, category_slug=None):
    category = get_object_or_404(Videocategory, slug=category_slug)
    videos = Video.objects.filter(category=category)
    return render(request, 'content/list.html', {'category': category, 'videos': videos})


def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    all_videos = Video.objects.all()

    if request.user.is_authenticated:
        VideoView.objects.get_or_create(user=request.user, video=video)
    context = {
        'video': video,
        'all_videos': all_videos,
        'VideoView': VideoView
        }

    return render(request, 'content/detail.html', context)
