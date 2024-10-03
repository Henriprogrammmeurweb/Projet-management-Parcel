from django.db import models
from AppProduct.models import Product
from AppAgency.models import Agency


class PackagesProduct(models.Model):
    """Classe qui présente les colis dans la base données"""
    sender = models.CharField(max_length=254)
    agency_passe = models.ManyToManyField(Agency)
    product_content = models.ManyToManyField(Product, through="AddProductToPackages")
    expected_shipping_date = models.DateField()

    def __str__(self) -> str:
        return self.sender


class AddProductToPackages(models.Model):
    """Classe reprente qui les produits ajouter à un colis"""
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    packages = models.ForeignKey(PackagesProduct, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.product.name
    

class FollowPackages(models.Model):
    """Classe qui réprente le suivi des colise dans la base de données"""
    packages = models.ForeignKey(PackagesProduct, on_delete=models.PROTECT)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT, blank=True, null=True)
    date_follow = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.packages.sender