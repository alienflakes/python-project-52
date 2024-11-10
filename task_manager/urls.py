from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    path('admin/', admin.site.urls)
]
