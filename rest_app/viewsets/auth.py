from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from permission.controllers.role_controller import UserRoleController
from permission.controllers.user_controller import create_password
from permission.models import RoleUser
from rest_app.serializers.auth import LoginSerializer, UserSerializer


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]


    @swagger_auto_schema(
        operation_description="Регистрация",
        request_body=LoginSerializer,
        responses={
            201: "Успешная регистрация",
            400: "Ошибка регистрации",
        }
    )
    @action(methods=["post"], detail=False)
    def registration(self, request):
        email = request.data["email"]
        username = email
        #password = request.data["password"]
        try:
            User.objects.get(email=email)
            return Response('Пользователь с таким email уже зарегистрирован', status=400)
        except User.DoesNotExist:
            password = create_password()
            password = User.objects.make_random_password()
            print(password)
            user = User.objects.create(email=email, username=username)
            user.password = password
            user.save()
            RoleUser.objects.create(user=user)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=201)

    @swagger_auto_schema(
        operation_description="Авторизация",
        request_body=LoginSerializer,
        responses={
            202: "Успешная авторизация",
            400: "Ошибка авторизации",
        }
    )
    @action(methods=["post"], detail=False)
    def login(self, request):

        username = request.data["email"]
        password = str(request.data["password"])
        print(authenticate(username=username, password=password))
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                try:
                    login(request, user)
                    UserRoleController(user).set_role()
                except UserRoleController.NotAccessException:
                    return Response({'detail': 'Нет доступа'}, 400)
                return Response(status=202)
        raise ParseError('Проверьте правильность введенных данных')

    @swagger_auto_schema(
        operation_description="Выход из системы",
        responses={
            202: "Успешный выход из системы",
            400: "Ошибка выхода из системы",
            401: "Вы не авторизованы",
        }
    )
    @action(methods=["post"], detail=False)
    def logout(self, request):
        user = request.user
        if user.is_authenticated:
            logout(request)
            return Response(status=202)
        return Response(status=404)