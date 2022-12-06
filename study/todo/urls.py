from . import views
from  django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('todo_list', views.todo_list, name="todo_list")
]
