from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from member.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'img_profile',
            'age',
        )


class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'age',
            'nickname',
            'token',
        )

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise ValidationError('Password Does Not Match!')
        return data

    def create(self, validated_data):

        return self.Meta.model.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password1'],
            age=validated_data['age'],
            nickname=validated_data['nickname'],
        )

    def get_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key

