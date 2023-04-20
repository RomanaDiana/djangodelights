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
]