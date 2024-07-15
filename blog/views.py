from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Articles
from .serializers import ArticlesSerializer, RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser

User = get_user_model()

class PublicArticlesList(generics.ListAPIView):
    queryset = Articles.objects.filter(is_public=True)
    serializer_class = ArticlesSerializer
    parser_classes = (MultiPartParser, FormParser)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser, FormParser)

class PrivateArticlesList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Articles.objects.filter(is_public=False)
    serializer_class = ArticlesSerializer
    parser_classes = (MultiPartParser, FormParser)

class ArticleCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()