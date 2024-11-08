from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    
class Plant(models.Model):
    class CategoryChoices(models.TextChoices):
        TREE = 'tree', 'Tree'
        FRUIT = 'fruit', 'fruit'
        VEGETABLES = 'vegetables', 'vegetables'
        FLOWER = 'flower', 'flower'
        HERBS = 'herbs', 'herbs'
    
    name= models.CharField(max_length=1024)
    about= models.TextField()
    used_for= models.TextField()
    image=models.ImageField(upload_to="images/", default="images/default.png")
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        default=CategoryChoices.TREE,
    )
    is_edible = models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)
    native_to = models.ManyToManyField(Country, blank=True)  # New field for countries
    
    
