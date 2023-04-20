from django.urls import path 
from . import views

urlpatterns = [
    path('ingredients/', views.IngredientView.as_view(), name='ingredients'),
    path('ingredients/new', views.CreateIngredientView.as_view(), name='create_ingredient'),
    path('ingredients/<int:pk>/update', views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('ingredients/<int:pk>/delete', views.DeleteIngredientView.as_view(), name='delete_ingredient'),
]