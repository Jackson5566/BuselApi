from django.db import models
from django.contrib.auth.models import User

from product_app.custom import FirebaseStorage


class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(default=None, storage=FirebaseStorage(), upload_to='products')
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()
    sold = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + str(self.id)
