# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("", views.Home, basename="home")
urlpatterns = [
    path("", include(router.urls)),
    path("", include("rest_framework.urls", namespace="rest")),
]
