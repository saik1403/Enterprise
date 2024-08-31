# urls.py
from django.urls import path
from .views import SigninView, SignoutView, UserCreateView, UserListView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'),
    path('signout/', SignoutView.as_view(), name='signout'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]
