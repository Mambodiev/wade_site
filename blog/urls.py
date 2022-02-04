from django.urls import path

from . import views
from blog.views import (
    like
)
app_name = 'blog'

urlpatterns = [
    path('post', views.post, name='post'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/', views.category_list, name='category_list'),
    path('like/<slug>/', like, name='like'),
]
