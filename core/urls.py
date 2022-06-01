from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

from core.views import (
        BlogLoginView,
        BlogAboutView,
        BlogSignupView,
        )

app_name = 'core'

urlpatterns = [
        path('contact/', views.ContactView.as_view(), name='contact'),
        path('login/', views.BlogLoginView.as_view(), name='login'),
        path('about/', views.BlogAboutView.as_view(), name='about'),
        path('signup/', views.BlogSignupView.as_view(), name='signup'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


