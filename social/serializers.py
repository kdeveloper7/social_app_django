from rest_framework import serializers
from .models import Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  # Obtiene el username del User

    class Meta:
        model = Post
        fields = ['id', 'content', 'created_at', 'user', 'username']  # Incluye username
