from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.UsersView.as_view(), name='users_view')
]
