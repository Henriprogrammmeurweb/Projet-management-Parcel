from django.db import models



class Category(models.Model):
    """Classe qui représente les catégories des articles dans la base de données"""
    designation = models.CharField(max_length=254, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.designation


class Product(models.Model):
    """Classe qui présente les produits dans la base de données"""
    name = models.CharField(max_length=254, unique=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=20, decimal_places=2)
    category_product = models.ForeignKey(Category, on_delete=models.PROTECT)
    

    def __str__(self) -> str:
        return self.name


