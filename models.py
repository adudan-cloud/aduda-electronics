from django.db import models

class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram_gb = models.IntegerField()
    storage_gb = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model}"


class Accessory(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.name}"


    

