"""
Serializers for the users API View.
"""
# from django.contrib.auth import (
#     get_user_model,
#     authenticate,
# )
# from django.utils.translation import gettext as _

from rest_framework import serializers
from core import models


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ['title', 'description', 'time_minutes', 'price', 'link']
