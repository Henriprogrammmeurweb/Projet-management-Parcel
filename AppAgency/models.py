from django.db import models


class Agency(models.Model):
    """Classe qui représente les agences de la base données"""
    name = models.CharField(max_length=254, unique=True)
    country = models.CharField(max_length=254)

    def __str__(self) -> str:
        return self.name
