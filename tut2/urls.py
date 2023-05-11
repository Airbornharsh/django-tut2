from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views 

urlpatterns = [
    path("token/", views.obtain_auth_token),
    path("", include("home.urls")),
    path("admin/", admin.site.urls),
]
