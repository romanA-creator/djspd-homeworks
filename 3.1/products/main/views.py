from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from .models import Product

@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()  # Получаем все товары
    serializer = ProductListSerializer(products, many=True)  # Сериализация списка товаров
    return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)  # Получение конкретного товара по ID
        except Product.DoesNotExist:
            return Response({"error": "Товар не найден"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductDetailsSerializer(product)  # Сериализация детальной информации о товаре
        return Response(serializer.data, status=status.HTTP_200_OK)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
