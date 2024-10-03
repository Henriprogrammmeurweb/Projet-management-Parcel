from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=254, unique=True)
    country = models.CharField(max_length=254)

    def __str__(self) -> str:
        return self.name
