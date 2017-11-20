from django.http import Http404
from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from member.serializer import UserSerializer
from post.utlis.permissions import IsAuthorOrReadOnly
from .models import Post
from .serializer import PostSerializer


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        # permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAuthenticated,
    )

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
    lookup_url_kwarg = 'post_pk'

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance in user.like_posts.filter(pk=instance.pk):
            user.like_posts.remove(instance)
            like_status = False
        else:
            user.like_posts.add(instance)
            like_status = True
        data = {
            'user': UserSerializer(user).data,
            'post': PostSerializer(instance).data,
            'result': like_status,
        }
        return Response(data)