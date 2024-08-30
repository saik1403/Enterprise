# serializers.py
from rest_framework import serializers
from exercise_1.models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'date_joined']
