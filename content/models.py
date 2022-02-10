from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model 
from django.db.models.signals import pre_save, post_save
from django.forms import ModelForm


# Create your models here.


class Video_category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Video_categories'
    
    def get_absolute_url(self):
        return reverse('content:course-list', args=[self.slug])

    def __str__(self):
        return self.name



class Video(models.Model):
    video_category = models.ForeignKey(Video_category, related_name='video', on_delete=models.CASCADE)
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(unique=True)
    description = models.TextField()
    related_video = models.ForeignKey(
        'self', related_name='related', on_delete=models.SET_NULL, blank=True, null=True)
    order = models.IntegerField(default=1)
    

    class Meta:
        verbose_name_plural = 'Videos'
        ordering = ["order"]    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('content:video_detail', args=[self.slug])
    
    @property
    def get_comments(self):
        return self.video_comment.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(video=self).count()

def pre_save_course(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


def pre_save_video(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


class Comment(models.Model):
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='')
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']