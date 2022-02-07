from django.contrib import admin
from .models import Video_category, Video


@admin.register(Video_category)
class Video_categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}