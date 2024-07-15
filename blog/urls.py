from django.urls import path
from .views import PublicArticlesList, RegisterView, PrivateArticlesList, ArticleCreateView, ArticleDetailView

urlpatterns = [
    path('articles/public/', PublicArticlesList.as_view(), name='public-articles'),
    path('register/', RegisterView.as_view(), name='register'),
    path('articles/private/', PrivateArticlesList.as_view(), name='private-articles'),
    path('articles/create/', ArticleCreateView.as_view(), name='create-article'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]