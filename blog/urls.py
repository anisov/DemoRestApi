from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('posts/', PostsListView.as_view(), name='all_posts'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', CreatePostView.as_view(), name='post_create'),
    path('user_posts/', UserPostsView.as_view(), name='own_posts'),
    path('user_posts/<int:user>/', UserPostsView.as_view(), name='user_posts'),
]
