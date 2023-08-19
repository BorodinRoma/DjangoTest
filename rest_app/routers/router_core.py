from rest_framework import routers

from rest_app.viewsets.core import *

router = routers.DefaultRouter(trailing_slash=False)
router.register('bookmark', BookmarkViewSet, basename='bookmark')
router.register('collection', CollectionViewSet, basename='collection')