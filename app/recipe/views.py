from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Recipe
from recipe.serializers import RecipeSerializer


class RecipeView(APIView):
    """List all recipes"""
    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.YTTP_400_BAD_REQUEST)
