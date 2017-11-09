from django.http import Http404
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializer import PostSerializer


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serialization):
        serialization.save(author=self.request.user)


class PostDetail(APIView):
    def get_object(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, post_pk, format=None):
        posts = self.get_object(post_pk)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    def put(self, request, post_pk, format=None):
        posts = self.get_object(post_pk)
        serializer = PostSerializer(posts, data=request.data, user=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk, format=None):
        posts = self.get_object(post_pk)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









