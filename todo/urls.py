from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [
    path('', views.index, name='home'),
    path('create-todo/', views.create_todo, name='create-todo'),
]