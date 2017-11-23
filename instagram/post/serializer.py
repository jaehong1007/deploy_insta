from rest_framework import serializers

from member.serializer import UserSerializer
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ('pk',
                  'photo',
                  'author',
                  'created_at',
                  )

