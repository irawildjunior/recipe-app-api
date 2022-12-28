"""
URL mappings for the recipe API.
"""
from django.urls import path

from recipe import views


app_name = 'recipe'

urlpatterns = [
    path('recipe-list/', views.RecipeView.as_view(), name='recipe-list'),
]
