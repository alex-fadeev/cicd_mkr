from django.urls import path
from .views import RecipeListView, RecipeDetailView, main, recipe_detail

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('main/', main, name='main'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe_detail/<int:pk>/', recipe_detail, name='recipe_detail'),
]
