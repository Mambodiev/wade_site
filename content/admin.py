from django.contrib import admin
from .models import Video_category, Video, Comment, VideoView, VideoLike


@admin.register(Video_category)
class Video_categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'approved', 'timestamp']
    list_editable = ['approved',]


@admin.register(VideoView)
class VideoViewAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(VideoLike)
class VideoLikeAdmin(admin.ModelAdmin):
    list_display = ['user']