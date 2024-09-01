# urls.py
from django.urls import path
from .views import (
    SignInView, RefreshTokenView,SignOutView, 
    UserCreateView, UserListView, UserRetrieveUpdateDestroyView,
    CountryListCreateView, CountryRetrieveUpdateDestroyView,
    StateListCreateView, StateRetrieveUpdateDestroyView,
    CityListCreateView, CityRetrieveUpdateDestroyView
)

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('refresh_token/', RefreshTokenView.as_view(), name='token_refresh'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),
    path('states/', StateListCreateView.as_view(), name='state-list-create'),
    path('states/<int:pk>/', StateRetrieveUpdateDestroyView.as_view(), name='state-detail'),
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('cities/<int:pk>/', CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),
]
