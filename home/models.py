# from uuid import *
from django.db import models

# Create your models here.

# class Base_Model(models.Model):
#     # uid = models.UUIDField(primary_key=True, editable=False,default=uuid4())
#     created_at = models.DateTimeField(auto_created=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     class META:
#         abstract = True


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)
