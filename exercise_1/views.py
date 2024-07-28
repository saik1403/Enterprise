from rest_framework import generics, pagination
from .models import User
from .serializers import UserSerializer

class UserCursorPagination(pagination.CursorPagination):
    page_size = 10
    ordering = 'id'

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserCursorPagination

    def perform_create(self, serializer):
        serializer.save()

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
