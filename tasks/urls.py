from django.urls import path
from .views import list_tasks, create_task, delete_task

urlpatterns = [
  path('', list_tasks),
  path('new/', create_task, name='create_task'),
  path('delete/<int:id>/', delete_task, name='delete_task'),
]