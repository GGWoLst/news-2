from django.urls import path
from .views import (
    NewsCreateView, ArticleCreateView, 
    PostUpdateView, PostDeleteView,
    news_list, news_search
)

urlpatterns = [
    path('', news_list, name='news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', PostDeleteView.as_view(), name='news_delete'),
    path('news/search/', news_search, name='news_search'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', PostUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', PostDeleteView.as_view(), name='article_delete'),
]
