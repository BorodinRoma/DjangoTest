"""Адреса в точке api/*"""
from django.conf.urls import include
from django.urls import re_path, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.controllers.core import create_urlpatterns
from rest_app.routers.router_auth import router as router_auth

schema_view = get_schema_view(
    openapi.Info(
        title="AUTH API",
        default_version='v0',
        description="API для авторизации",
    ),
    patterns=[
        re_path(r'^api/', include('rest_app.urls_auth')),
    ],
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

routers = [
    (r'^auth/', router_auth),

]

urlpatterns = [
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
              ] + create_urlpatterns(routers)
