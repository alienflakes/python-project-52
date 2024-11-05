from django.urls import path
from . import views


urlpatterns = [
    path('', views.UsersView.as_view(), name='users'),
    path('create/', views.SignUpView.as_view(), name='signup'),
    path('<int:id>/update/', views.CustomUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/')
]
