from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('<int:pk>', views.TaskView.as_view(), name='task_view'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(),
         name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(),
         name='task_delete')
]
