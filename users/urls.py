from django.urls import path
from . import views


urlpatterns = [
    path('', views.UsersView.as_view(), name='users_view'),
    path('create/', views.SignUpView.as_view(), name='signup'),
    # path('<int:pk>/update/'),
    # path('<int:pk>/delete/')
]
