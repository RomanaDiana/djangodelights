from django.urls import path 
from . import views

urlpatterns = [
    path('ingredients/', views.IngredientView.as_view(), name='ingredients'),
    path('ingredients/new', views.CreateIngredientView.as_view(), name='create_ingredient'),
    path('ingredients/<int:pk>/update', views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('ingredients/<int:pk>/delete', views.DeleteIngredientView.as_view(), name='delete_ingredient'),
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/new', views.CreateMenuItemView.as_view(), name='create_menu_item'),
    path('menu/<int:pk>/update', views.UpdateMenuItemView.as_view(), name='update_menu_item'),
    path('menu/<int:pk>/delete', views.DeleteMenuItemView.as_view(), name='delete_menu_item'),
    path('recipe_requirements/', views.RecipeRequirementView.as_view(), name='recipe_requirements'),
    path('recipe_requirements/new', views.CreateRecipeRequirementView.as_view(), name='create_recipe_requirement'),
    path('recipe_requirement/<int:pk>/update', views.UpdateRecipeRequirementView.as_view(), name='update_recipe_requirement'),
    path('recipe_requirement/<int:pk>/delete', views.DeleteRecipeRequirementView.as_view(), name='delete_recipe_requirement'),
    path('purchases', views.PurchaseView.as_view(), name='purchases'),
    path('purchases/new', views.CreatePurchaseView.as_view, name='create_purchase'),
    path('purchases/<int:pk>/update', views.UpdatePurchaseView.as_view(), name='update_purchase'),
    path('purchases/<int:pk>/delete', views.DeletePurchaseView.as_view(), name='delete_purchase'),
]