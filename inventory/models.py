import datetime
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()

    def __str__(self):
        return f"""
        name = {self.name};
        quantity = {self.quantity};
        unit = {self.unit};
        unit_price = {self.unit_price};
        """


class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()
    image_url = models.URLField(max_length=200, null=True, blank=True)
    recipe_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"title = {self.title}; price = {self.price}"


    def available(self):
        return all(
            X.enough() for X in self.RecipeRequirement_set.all()
        )


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"menu_item = [{self.menu_item.__str__()}]; ingredient = {self.ingredient.name}; quantity = {self.quantity}"

    def enough(self):
        return self.quantity <= self.ingredient.quantity


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.date)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; timestamp = {self.timestamp}"
