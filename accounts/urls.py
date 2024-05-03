from django.urls import path
from .views import LoginAPI, RegisterAPI, ChangePasswordView, UserAPI, UserListAPI

urlpatterns = [
    path('login/', LoginAPI.as_view(), name="login"),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('reset/', ChangePasswordView.as_view(), name='reset'),
    path('users/<int:id>/', UserAPI.as_view(), name='user'),
    path('users/', UserListAPI.as_view(), name='users'),
]