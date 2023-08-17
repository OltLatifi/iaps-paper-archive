from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("archive.urls")),
    path("admin/", admin.site.urls),
]
