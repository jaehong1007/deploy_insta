from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializer import PostSerializer


class PostList(APIView):

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)



