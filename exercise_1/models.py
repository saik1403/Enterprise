from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class MyUserManager(BaseUserManager):
    def create_user(self, email: str, password: str = None, **extra_fields) -> 'MyUser':
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str = None, **extra_fields) -> 'MyUser':
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        return self.email


class Country(models.Model):
    id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name: str = models.CharField(max_length=100)
    country_code: str = models.CharField(max_length=3)
    curr_symbol: str = models.CharField(max_length=3)
    phone_code: str = models.CharField(max_length=5)
    my_user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='countries' )

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
