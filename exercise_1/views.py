# views.py
from rest_framework import generics, status
from rest_framework.pagination import CursorPagination
from exercise_1.models import MyUser,Country, State, City
from .serializers import UserSerializer, SigninSerializer, CountrySerializer, StateSerializer, CitySerializer
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


class GenericPagination(CursorPagination):
    page_size = 10
    ordering = 'name' 

class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = GenericPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(my_user=self.request.user)  

    def perform_create(self, serializer):
        serializer.save(my_user=self.request.user)  

class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(my_user=self.request.user) 
    
class StateListCreateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    pagination_class = GenericPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(country__my_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()  

class StateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(country__my_user=self.request.user)


class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = GenericPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(my_state__country__my_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()

class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(state__country__my_user=self.request.user)
