from django.db import models
import uuid

class User(models.Model):
    Email: str = models.CharField(max_length=50)

    @property
    def username(self):
        return self.Email

    @username.setter
    def set_username(self, username):
        self.Email = username

    def __str__(self) -> str:
        return self.Email

class Country(models.Model):
    id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name: str = models.CharField(max_length=100)
    country_code: str = models.CharField(max_length=3)
    curr_symbol: str = models.CharField(max_length=3)
    phone_code: str = models.CharField(max_length=5)
    my_user: User = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name: str = models.CharField(max_length=100)
    state_code: str = models.CharField(max_length=10)
    gst_code: str = models.CharField(max_length=5)
    country: Country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name: str = models.CharField(max_length=100)
    city_code: str = models.CharField(max_length=10)
    phone_code: str = models.CharField(max_length=10)
    population: int = models.IntegerField()
    avg_age: float = models.FloatField()
    num_of_adult_males: int = models.IntegerField()
    num_of_adult_females: int = models.IntegerField()
    state: State = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self) -> str:
        return self.name
