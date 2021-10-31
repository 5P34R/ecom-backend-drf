from django.db import models


class Catagory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
