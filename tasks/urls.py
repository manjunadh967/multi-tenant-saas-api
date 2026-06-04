from django.urls import path

from .views import (
    TaskListCreateView,
    TaskDetailView
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:id>/', TaskDetailView.as_view()),
]