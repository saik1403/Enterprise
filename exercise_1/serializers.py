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
    
class CitySerializer(serializers.ModelSerializer):
    state__name = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ['id', 'name', 'city_code', 'phone_code', 'population', 'avg_age', 'num_of_adult_males', 'num_of_adult_females','state', 'state__name']

    def get_state__name(self, obj):
        return obj.state.name
    
    def validate(self, data):
        # Validate that population is greater than the sum of adult males and females
        if data['population'] < (data['num_of_adult_males'] + data['num_of_adult_females']):
            raise serializers.ValidationError("Population must be greater than the sum of adult males and females.")

        return data

    def validate_city_code(self, value):
        # Validate that city_code is unique within a state
        if City.objects.filter(city_code=value, state=self.instance.state).exists():
            raise serializers.ValidationError("City code must be unique within a state.")
        return value
class StateSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)
    country__name = serializers.SerializerMethodField()
    country__my_user__name = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = ['id', 'name', 'state_code', 'gst_code','country', 'country__name', 'country__my_user__name','cities']

    def get_country__name(self, obj):
        return obj.country.name

    def get_country__my_user__name(self, obj):
        return obj.country.my_user.email
    
    def validate_name(self, value):
        # Validate that state name is unique within a country
        if State.objects.filter(name=value, country=self.instance.country).exists():
            raise serializers.ValidationError("State name must be unique within a country.")
        return value

    def validate_gst_code(self, value):
        # Validate that GST code is unique
        if State.objects.filter(gst_code=value).exists():
            raise serializers.ValidationError("GST code must be unique.")
        return value



class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True)
    class Meta:
        model = Country
        fields = ['id', 'name', 'country_code', 'curr_symbol', 'phone_code','states']

    def validate_country_code(self, value):
        # Validate that country code is unique
        if Country.objects.filter(country_code=value).exists():
            raise serializers.ValidationError("Country code must be unique.")
        return value

    def validate_phone_code(self, value):
        # Validate that phone code is unique
        if Country.objects.filter(phone_code=value).exists():
            raise serializers.ValidationError("Phone code must be unique.")
        return value

    def create(self, validated_data):
        states_data = validated_data.pop('states')
        country = Country.objects.create(**validated_data)

        for state_data in states_data:
            cities_data = state_data.pop('cities')
            state = State.objects.create(country=country, **state_data)

            for city_data in cities_data:
                City.objects.create(state=state, **city_data)

        return country

    def update(self, instance, validated_data):
        states_data = validated_data.pop('states')

        # Update country fields
        instance.name = validated_data.get('name', instance.name)
        instance.country_code = validated_data.get('country_code', instance.country_code)
        instance.curr_symbol = validated_data.get('curr_symbol', instance.curr_symbol)
        instance.phone_code = validated_data.get('phone_code', instance.phone_code)
        instance.save()

        # Update or create states and cities
        for state_data in states_data:
            state, created = State.objects.update_or_create(
                country=instance,
                name=state_data.get('name'),
                defaults={'state_code': state_data.get('state_code'), 'gst_code': state_data.get('gst_code')}
            )

            cities_data = state_data.get('cities')
            for city_data in cities_data:
                City.objects.update_or_create(
                    state=state,
                    name=city_data.get('name'),
                    defaults={
                        'city_code': city_data.get('city_code'),
                        'phone_code': city_data.get('phone_code'),
                        'population': city_data.get('population'),
                        'avg_age': city_data.get('avg_age'),
                        'num_of_adult_males': city_data.get('num_of_adult_males'),
                        'num_of_adult_females': city_data.get('num_of_adult_females')
                    }
                )
        return instance
