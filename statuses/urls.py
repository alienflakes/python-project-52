from django.urls import path
from . import views


urlpatterns = [
    path('', views.StatusListView.as_view(), name='st_list'),
    path('create/', views.StatusCreateView.as_view(), name='st_create'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='st_update'),
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(), name='st_delete')
]
