from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo')

urlpatterns = [
    path("todo", TodoView.as_view()),
]

urlpatterns += router.urls
