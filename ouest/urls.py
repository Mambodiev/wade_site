from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from blog.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls', namespace='core')),
    path('', include('blog.urls', namespace='blog')),
    path('content/', include('content.urls', namespace='content')),
    path('_ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
]


<<<<<<< HEAD
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
                    
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68

