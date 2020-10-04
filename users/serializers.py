from django.contrib.auth.models import update_last_login
from django.core.cache import cache
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_login', 'last_activity']

    last_activity = serializers.SerializerMethodField()

    def get_last_activity(self, obj):
        return cache.get(obj.username)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        update_last_login(None, user)
        return token


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        token = super().validate(attrs)
        jwt = JWTAuthentication()
        validated_token = jwt.get_validated_token(token['access'])
        user = jwt.get_user(validated_token)
        update_last_login(None, user)
        return token
