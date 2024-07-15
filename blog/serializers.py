from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Articles
from django.db import IntegrityError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_author']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        username = validated_data.get('username', validated_data['email'].split('@')[0])
        original_username = username
        counter = 1

        while User.objects.filter(username=username).exists():
            username = f"{original_username}{counter}"
            counter += 1

        try:
            user = User.objects.create_user(
                username=username,
                email=validated_data['email'],
                password=validated_data['password']
            )
        except IntegrityError:
            raise serializers.ValidationError("A user with that email already exists.")

        return user
class ArticlesSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Articles
        fields = '__all__'