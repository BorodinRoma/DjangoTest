from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.controllers.bookmark_controller import BookmarkController
from core.controllers.collection_controller import CollectionController
from core.models import *
from core.models import Collection
from permission.controllers.permission_controller import IsAdmin, IsUser

from rest_app.serializers.core import BookmarkSerializer, BookmarkCreateSerializer, CollectionSerializer, \
    CollectionCreateSerializer, CollectionUpdateSerializer, AddBookmarkSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin | IsUser]
    queryset = Bookmark.objects.all()
    http_method_names = ['post', 'get', 'patch', 'delete']
    serializer_class = BookmarkSerializer

    @swagger_auto_schema(
        operation_description='Создание закладки',
        request_body=BookmarkCreateSerializer,
        responses={
            201: "Закладка успешно создана",
            400: "Ошибка"
        }

    )
    def create(self, request, *args, **kwargs):
        current_user = request.user
        url = request.data['url']
        bookmark = BookmarkController(current_user).create_bookmark(url)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description='Обновить закладку',
        responses={
            201: "Закладка успешно обновлена",
            400: "Ошибка"
        }

    )
    def partial_update(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(
        operation_description='Получить закладки',
        responses={
            200: BookmarkSerializer(many=True)
        }
    )
    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(created_by=request.user)
        serializers = BookmarkSerializer(queryset, many=True)
        return Response(serializers.data, status=200)

    @swagger_auto_schema(
        operation_description='Удалить закладку',
        responses={
            204: 'Успешное удаление',
            404: 'Не найдена закладка',
        }
    )
    def destroy(self, request, pk=None):
        try:
            user = request.user
            BookmarkController(user).destroy(pk)
        except BookmarkController.NotAccessException as e:
            raise Exception(str(e))


class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin | IsUser]
    queryset = Collection.objects.all()
    http_method_names = ['post', 'get', 'patch', 'delete']
    serializer_class = CollectionSerializer

    @swagger_auto_schema(
        operation_description='Создание коллекции',
        request_body=CollectionCreateSerializer,
        responses={
            201: "Коллекция успешно создана",
            400: "Ошибка"
        }

    )
    def create(self, request, *args, **kwargs):
        current_user = request.user
        collection = CollectionController(current_user).create_collection(request.data)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description='Обновить название и описание коллекции',
        request_body=CollectionUpdateSerializer,
        responses={
            201: "Коллекция успешно обновлена",
            400: "Ошибка"
        }

    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, args, kwargs)

    @swagger_auto_schema(
        operation_description='Добавить закладку в коллекцию',
        request_body=AddBookmarkSerializer,
        responses={
            201: "Коллекция успешно обновлена",
            400: "Ошибка"
        }

    )
    @action(methods=['post'], detail=False)
    def add_bookmark(self, request):
        current_user = request.user
        collection = CollectionController(current_user).add_bookmarks(request.data)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=201)

    @swagger_auto_schema(
        operation_description='Удалить закладку из коллекции',
        request_body=AddBookmarkSerializer,
        responses={
            201: "Коллекция успешно обновлена",
            400: "Ошибка"
        }

    )
    @action(methods=['post'], detail=False)
    def delete_bookmark(self, request):
        current_user = request.user
        CollectionController(current_user).delete_bookmarks(request.data)
        return Response('Закладки удалены', status=201)
    #
    # @swagger_auto_schema(
    #     operation_description='Получить закладки',
    #     responses={
    #         200: BookmarkSerializer(many=True)
    #     }
    # )
    # def list(self, request, *args, **kwargs):
    #     queryset = self.queryset.filter(created_by=request.user)
    #     serializers = BookmarkSerializer(queryset, many=True)
    #     return Response(serializers.data, status=200)
    #
    # @swagger_auto_schema(
    #     operation_description='Удалить закладку',
    #     responses={
    #         204: 'Успешное удаление',
    #         404: 'Не найдена закладка',
    #     }
    # )
    # def destroy(self, request, pk=None):
    #     try:
    #         user = request.user
    #         BookmarkController(user).destroy(pk)
    #     except BookmarkController.NotAccessException as e:
    #         raise Exception(str(e))