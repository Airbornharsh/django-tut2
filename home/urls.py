from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("get-todos", get_todos, name="get_todos"),
    path("post-todo", post_todo, name="post_todo"),
]
