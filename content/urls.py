from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
        path('addcomment/<int:id>', views.addcomment, name='addcomment'),
        path('video', views.video, name='video'),
        path('<slug:slug>', views.video_detail, name='video_detail'),
        path('<slug:category_slug>/', views.category_list, name='category_list'),
        # path('course/', views.CourseListView.as_view(), name='course-list'),
        # path('<slug>/', views.CourseDetailView.as_view(), name='course-detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


