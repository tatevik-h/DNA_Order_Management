from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer


class SignupView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeactivateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response({'message': 'User deactivated'})
