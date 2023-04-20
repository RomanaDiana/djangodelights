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


class MenuItemView(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


class CreateMenuItemView(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    fields = ["title", "price", "image_url", "recipe_url"]


class UpdateMenuItemView(UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update_form.html"
    fields = ["title", "price", "image_url", "recipe_url"]


class DeleteMenuItemView(DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menu')