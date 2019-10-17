from rest_framework import generics
from blog.models import Blog
from blog.serializers import PostsListSerializer, PostDetailSerializer
from common.permissions import IsOwnerOrReadOnly


class PostsListView(generics.ListAPIView):
    serializer_class = PostsListSerializer
    queryset = Blog.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Blog.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class CreatePostView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer


class UserPostsView(generics.ListAPIView):
    serializer_class = PostsListSerializer
    queryset = Blog.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        user = self.kwargs.get('user', False)
        if user:
            queryset = queryset.filter(user_id=user)
        else:
            queryset = queryset.filter(user=self.request.user)
        return queryset



