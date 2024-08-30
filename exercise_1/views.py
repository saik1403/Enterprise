# views.py
from rest_framework import generics
from rest_framework.pagination import CursorPagination
from exercise_1.models import MyUser
from .serializers import UserSerializer

# Custom Cursor Pagination class
class UserCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'date_joined'  # Cursor pagination requires an ordering field

# List/Create View
class UserListCreateView(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserCursorPagination

# Retrieve/Update/Destroy View
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer