from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('_ckeditor/', include('ckeditor_uploader.urls')),
    path('core', include('core.urls')),
    path('', views.post_all, name='post_all'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)