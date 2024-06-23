from django.urls import path,include
from rest_framework.routers import DefaultRouter
from.views import BookApi

router = DefaultRouter()
router.register("", BookApi)

urlpatterns = [
    path('', include(router.urls)),

]
