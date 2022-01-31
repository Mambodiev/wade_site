#from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('blog:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Post(models.Model):
        category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
        created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_creator')
        title = models.CharField(max_length=255)
        author = models.CharField(max_length=255, default='admin')
        about_author = models.CharField(max_length=255, default='An editor at Blogzine')
        description = RichTextUploadingField(blank=True, null=True)
        short_description = models.CharField(max_length=255)
        category_name = models.CharField(max_length=255)
        image = models.ImageField(upload_to='images/', default='images/default.png')
        slug = models.SlugField(max_length=255, blank=True, null=True,)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        time_read = models.CharField(max_length=255, default='5 min read')
        is_left_big_card = models.BooleanField(default=False)
        is_right_medium_cards = models.BooleanField(default=False)
        is_right_left_small_cards = models.BooleanField(default=False)
        is_right_right_small_cards = models.BooleanField(default=False)
        is_today_top_highlights = models.BooleanField(default=False)
        active = models.BooleanField(default=False)

        class Meta:
            #verbose_name_plural = 'Post'
            ordering = ('-created',)

        def get_absolute_url(self):
            return reverse('blog:post_detail', args=[self.slug])

        def __str__(self):
            return self.title




