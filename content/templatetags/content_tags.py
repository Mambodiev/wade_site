from django import template
from content.models import Video

register = template.Library()

@register.inclusion_tag('content/content/recent_video.html')
def show_recent_videos():
    recent_videos = Video.objects.all().order_by('id')[:3]
    return {'recent_videos': recent_videos}