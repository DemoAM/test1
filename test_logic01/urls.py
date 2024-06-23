from django.contrib import admin
from django.urls import path, include
from user import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# from user.views import get_author_user,create_author_user
urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', get_author_user, name="home"),
    # path('add/', create_author_user, name="add"),
]
