from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/', views.category_list, name='category_list'),
]
