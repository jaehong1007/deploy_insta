from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from member.serializer import UserSerializer, SignupSerializer

User = get_user_model()


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            token, token_created = Token.objects.get_or_create(
                user=user,
            )

            data = {
                'token': token.key,
                'user': UserSerializer(user).data
            }
            return Response(data, status=status.HTTP_200_OK)
        data = {
            'message': 'Invalid Authentication'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)


class Signup(APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # username = request.data['username']
        # password = request.data['password']
        # password2 = request.data['password2']
        # age = request.data['age']
        #
        # if User.objects.filter(username=username).exists():
        #     return Response({'messages': 'Username already exist'})
        #
        # user = User.objects.create_user(
        #     username=username,
        #     password=password,
        #     password2=password2,
        #     age=age,
        # )
        # token = Token.objects.create(user=user)
        # data = {
        #     'user': SignupSerializer(user).data,
        #     'token': token.key
        # }
        # return Response(data)