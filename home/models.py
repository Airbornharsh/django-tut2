# from uuid import *
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Base_Model(models.Model):
#     # uid = models.UUIDField(primary_key=True, editable=False,default=uuid4())
#     created_at = models.DateTimeField(auto_created=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     class META:
#         abstract = True


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)


class TimingTodo(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    timing = models.DateTimeField()
