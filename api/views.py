from django.shortcuts import render
from rest_framework import status, permissions, generics, viewsets
from .sirealizers import UserSerialier, CategorySirializer, TaskSerialializer, ProfileSerializer
from rest_framework.response import Response
from .models import Task, Category, Profile
from django.contrib.auth.models import User
from . import permission

# userを作るための
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerialier
    permission_classes = (permissions.AllowAny,)

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialier

class LoginUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerialier
    
    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        response = {'message': 'PUT method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELEtE method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySirializer

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELETE method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message': 'PUT method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialializer
    permission_class = (permissions.IsAuthenticated, permission.OwnerPermission,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)