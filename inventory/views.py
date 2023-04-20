from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/Ingredient.html"    


class CreateIngredientView(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    fields = ["name", "quantity", "unit", "unit_price"]


class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    fields = ["name", "quantity", "unit", "unit_price"]


class DeleteIngredientView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy("ingredients")