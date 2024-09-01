# serializers.py
from rest_framework import serializers
from exercise_1.models import MyUser,Country,State,City
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'date_joined']

class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        print("email", email, "password", password)
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials")
            data['user'] = user
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")
        return data
    
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'country_code', 'curr_symbol', 'phone_code']

class StateSerializer(serializers.ModelSerializer):
    country__name = serializers.SerializerMethodField()
    country__my_user__name = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = ['id', 'name', 'state_code', 'gst_code','country', 'country__name', 'country__my_user__name']

    def get_country__name(self, obj):
        return obj.country.name

    def get_country__my_user__name(self, obj):
        return obj.country.my_user.email

class CitySerializer(serializers.ModelSerializer):
    state__name = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ['id', 'name', 'city_code', 'phone_code', 'population', 'avg_age', 'num_of_adult_males', 'num_of_adult_females','state', 'state__name']

    def get_state__name(self, obj):
        return obj.state.name