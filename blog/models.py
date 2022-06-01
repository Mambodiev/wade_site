from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model 
from django.forms import ModelForm


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
<<<<<<< HEAD
<<<<<<< HEAD
    image = models.ImageField(upload_to='media/', default='images/default.png')
=======
    image = models.ImageField(upload_to='media/',  blank=True, null=True)
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68
=======
    image = models.ImageField(upload_to='media/',  blank=True, null=True)
>>>>>>> s3success
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('blog:category_list', args=[self.slug])

    def __str__(self):
        return self.name







class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
<<<<<<< HEAD
    profile_picture = models.ImageField(upload_to='media/', default='images/default.png')
    about_author = models.TextField(default='Wade est rédacteur en chef du blogzine et fait également des reportages sur les dernières nouvelles basées à Londres.')
=======
    profile_picture = models.ImageField(upload_to='media/', blank=True, null=True)
    about_author = models.TextField(blank=True, null=True)
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68
=======
    profile_picture = models.ImageField(upload_to='media/', blank=True, null=True)
    about_author = models.TextField(blank=True, null=True)
>>>>>>> s3success


    def __str__(self):
        return self.user.username



        

class Post(models.Model):
        category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
        category_name = models.CharField(max_length=255)
        created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_creator')
        title = models.CharField(max_length=255)
<<<<<<< HEAD
<<<<<<< HEAD
        thumbnail = models.ImageField(upload_to='media/', default='images/default.png')
=======
        thumbnail = models.ImageField(upload_to='media/')
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68
=======
        thumbnail = models.ImageField(upload_to='media/')
>>>>>>> s3success
        slug = models.SlugField(max_length=255, blank=True, null=True,)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        about_author = models.CharField(max_length=255)
        description = RichTextUploadingField(blank=True, null=True)
        overview = models.CharField(max_length=255)
        comment_count=models.IntegerField(default=0)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        time_read = models.CharField(max_length=255)
        is_left_big_card = models.BooleanField(default=False)
        is_right_medium_cards = models.BooleanField(default=False)
        is_right_left_small_cards = models.BooleanField(default=False)
        is_right_right_small_cards = models.BooleanField(default=False)
        is_today_top_highlights = models.BooleanField(default=False)
        active = models.BooleanField(default=False)
        related_post = models.ForeignKey(
        'self', related_name='related', on_delete=models.SET_NULL, blank=True, null=True)
        previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
        next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

        class Meta:
            #verbose_name_plural = 'Post'
            ordering = ('-created',)

        def get_absolute_url(self):
            return reverse('blog:post_detail', args=[self.slug])
        
        def get_like_url(self):
            return reverse("like", kwargs={
                'slug': self.slug
            })
        
        
        @property
        def get_comments(self):
            return self.comments.all().order_by('-timestamp')

        @property
        def comment_count(self):
            return Comment.objects.filter(post=self).count()

        @property
        def get_view_count(self):
            return self.postview_set.all().count()

        
        @property
        def get_like_count(self):
            return self.like_set.all().count()



        def __str__(self):
            return self.title





class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_post', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='')
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)
    approved=models.BooleanField(default=False)


    def __str__(self):
        return self.user.username


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

