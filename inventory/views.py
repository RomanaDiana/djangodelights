from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Ingredients'] = Ingredient.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['recipe_requirements'] = RecipeRequirement.objects.all()
        context['purchases'] = Purchase.objects.all()
        return context


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


class RecipeRequirementView(ListView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement.html"


class CreateRecipeRequirementView(CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create_form.html"
    

class UpdateRecipeRequirementView(UpdateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_update_form.html"


class DeleteRecipeRequirementView(DeleteView):
    model = RecipeRequirement
    success_url = reverse_lazy('recipe_requirements')


class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchase.html"


class CreatePurchaseView(CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    fields = ["menu_item", "timestamp"]


class UpdatePurchaseView(UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    fields = ["menu_item", "timestamp"]


class DeletePurchaseView(DeleteView):
    model = Purchase
    success_url = reverse_lazy('purchases')