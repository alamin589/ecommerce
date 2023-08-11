# from django.conf.urls import url, include
from django.urls import include, path
from api import views
from rest_framework import routers
from django.urls import re_path

from django.urls import path

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewset)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
