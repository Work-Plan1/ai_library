from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']

    password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(min_length=8, write_only=True)

    def validate(self, attrs):
        pas1 = attrs['password']
        pas2 = attrs['confirm_password']
        email = attrs['email']
        if User.objects.filter(email=email):
            raise exceptions.AuthenticationFailed(
                {'success': False, 'message': 'This username already exist'})
        if pas1 != pas2:
            raise exceptions.AuthenticationFailed({'success': False, 'message': 'Passwords didn\'t match'})
        return attrs

    def create(self, validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise exceptions.AuthenticationFailed({'success': False, 'message': 'Username or password incorrect'})
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['old_password', 'password', 'confirm_password']

    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(required=True, min_length=8)

    def validate(self, attrs):
        pas1 = attrs['password']
        pas2 = attrs['confirm_password']
        if pas1 != pas2:
            raise exceptions.AuthenticationFailed({'message': 'Confirm password doesn\'t match!'})
        return attrs


