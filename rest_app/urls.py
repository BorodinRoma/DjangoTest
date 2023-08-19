from django.urls import re_path, include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.controllers.core import create_urlpatterns
from rest_app.routers.router_core import router as router_core

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API",
    ),
    patterns=[
        re_path(r'^api/v1/', include('rest_app.urls')),
    ],
    public=True,
    permission_classes=[permissions.IsAuthenticated, ],
)

routers = [
    (r'^core/', router_core),

]

urlpatterns = [
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
              ] + create_urlpatterns(routers)