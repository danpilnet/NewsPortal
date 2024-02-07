from django.urls import path
from .views import PostDetail, PostList, PostFilter, PostCreate, PostUpdate, PostDelete, PostSearch, ArticlesDetail



urlpatterns = [
   path('post/', PostList.as_view(), name='post_list'),
   path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('post/search/', PostSearch.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
   path('articles/<int:pk>/', ArticlesDetail.as_view()),
]

