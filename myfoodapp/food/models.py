from django.db import models

# Create your models here.

class Item(models.Model):
    
    def __str__(self) -> str:
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_descp = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://cdn-icons-png.flaticon.com/512/1147/1147805.png")