from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('content:course-list', args=[self.slug])

    def __str__(self):
        return self.name



class Video(models.Model):
    category = models.ForeignKey(Category, related_name='video', on_delete=models.CASCADE)
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(unique=True)
    description = models.TextField()
    order = models.IntegerField(default=1)
    

    class Meta:
        verbose_name_plural = 'Videos'
        ordering = ["order"]    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('content:video_detail', args=[self.slug])

def pre_save_course(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


def pre_save_video(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
