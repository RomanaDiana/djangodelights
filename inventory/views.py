from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.db.models import Sum
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


class CreatePurchaseView(TemplateView):
    template_name = "inventory/purchase_create_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
        return context
    
    def check(self, request):
        menu_item_id = request.POST["menu_item"] #Whether menu_item was submitted
        menu_item = MenuItem.objects.get(pk=menu_item_id) #get the id of an item from the form
        requirements = menu_item.reciperequirement_set #get all reciperequirement instances related to that id
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity #inventory minus requirement
            required_ingredient.save()

        purchase.save()
        

class UpdatePurchaseView(UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    fields = ["menu_item", "timestamp"]


class DeletePurchaseView(DeleteView):
    model = Purchase
    success_url = reverse_lazy('purchases')


class ReportView(TemplateView):
    template_name = "inventory/report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue = Sum("menu_item__price")
        )
        total_cost = 0
        for purchase in Purchase.objects.all():
            for reciperequirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += reciperequirement.ingredient.unit_price * \
                    reciperequirement.quantity
        
        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context