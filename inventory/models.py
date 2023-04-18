import datetime
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()


class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()
    image_url = models.URLField(max_length=200, null=True, blank=True)
    recipe_url = models.URLField(max_length=200, null=True, blank=True)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.date)
