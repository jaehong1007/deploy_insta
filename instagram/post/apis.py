from django.http import Http404
from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from post.utlis.permissions import IsAuthorOrReadOnly
from .models import Post
from .serializer import PostSerializer


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serialization):
        serialization.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
    )


class PostLikeToggle(generics.GenericAPIView):
    queryset = Post.objects.all()









