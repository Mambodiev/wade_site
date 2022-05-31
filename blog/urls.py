from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from blog.views import (
    like
)
app_name = 'blog'

urlpatterns = [
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('', views.home, name='home'),
    path('post', views.post, name='post'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/', views.category_list, name='category_list'),
    path('like/<slug>/', like, name='like'),
    
]
<<<<<<< HEAD
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======

handler404 = "blog.views.page_not_found_view"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68

