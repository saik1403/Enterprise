# views.py
from rest_framework import generics, status
from rest_framework.pagination import CursorPagination
from exercise_1.models import MyUser
from .serializers import UserSerializer, SigninSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import logout

class SigninView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SigninSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Custom Cursor Pagination class
class UserCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'date_joined'  # Cursor pagination requires an ordering field

# User Create (Allow Any)
class UserCreateView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# User List/Retrieve/Update/Destroy (Require Authentication)
class UserListView(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserCursorPagination
    permission_classes = [IsAuthenticated]

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]