

from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, LoginAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-retrieve-update-destroy'),
     path('login/', LoginAPIView.as_view(), name='api-login'),
]