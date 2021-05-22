from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [
    path('', views.index, name='home'),
    path('create-todo/', views.create_todo, name='create-todo'),
    path('detail-todo/<int:id>/', views.todo_detail, name='todo-detail'),
    path('delete-todo/<int:id>/', views.todo_delete, name='todo-delete'),
    path('edit-todo/<int:id>/', views.todo_edit, name='todo-edit'),
]