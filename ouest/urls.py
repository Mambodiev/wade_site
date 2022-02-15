from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('core/', include('core.urls', namespace='core')),
    path('', include('blog.urls', namespace='blog')),
    path('content/', include('content.urls', namespace='content')),
    path('_ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


