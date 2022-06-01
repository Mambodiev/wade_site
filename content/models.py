from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth import get_user_model 


User = get_user_model()


class VideoView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Videocategory(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Videocategories'
    
    def get_absolute_url(self):
        return reverse('content:course-list', args=[self.slug])

    def __str__(self):
        return self.name



class Video(models.Model):
    videocategory = models.ForeignKey(Videocategory, related_name='videocat', on_delete=models.CASCADE)
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
<<<<<<< HEAD
<<<<<<< HEAD
    image = models.ImageField(upload_to='media/', default='images/default.png')
=======
    image = models.ImageField(upload_to='media/')
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68
=======
    image = models.ImageField(upload_to='media/')
>>>>>>> s3success
    slug = models.SlugField(unique=True)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    # comment_count=models.IntegerField(default=0)
    view_count=models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)

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
        return self.comment.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(video=self).count() 

    @property
    def get_view_count(self):
        return self.videoview_set.all().count()

    @property
    def view_count(self):
            return VideoView.objects.filter(video=self).count()

        
    @property
    def get_like_count(self):
        return self.videolike_set.all().count()



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


# class VideoView(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     video = models.ForeignKey(Video, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


class VideoLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


