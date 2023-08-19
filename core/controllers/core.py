from django.urls import re_path, include
from rest_framework.routers import BaseRouter


def create_urlpatterns(routers: (str, BaseRouter)) -> []:
    urlpatterns = []
    for name, router in routers:
        urlpatterns.append(
            re_path(name, include(router.urls)),
        )
    return urlpatterns


