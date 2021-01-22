from rest_framework import routers
from django.urls import path, include
from .views import TaskViewSet, CategoryViewSet, CreateUserView, ListUserView, LoginUserView, ProfileViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tasks', TaskViewSet)
router.register('profile', ProfileViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='lusers'),
    path('login/', LoginUserView.as_view(), name='login'),
]