from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/posts/recent_post.html')
def show_recent_posts():
    recent_posts = Post.objects.all().order_by('id')[:4]
    return {'recent_posts': recent_posts}