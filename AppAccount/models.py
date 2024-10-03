from django.db import models
from django.contrib.auth.models import AbstractUser
from AppAgency.models import Agency



class UserAccount(AbstractUser):
    username = models.CharField(max_length=254)
    last_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=254, unique=True)
    user_agency = models.ForeignKey(Agency, on_delete=models.PROTECT)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'last_name', 'password']


    def __str__(self) -> str:
        return self.username
