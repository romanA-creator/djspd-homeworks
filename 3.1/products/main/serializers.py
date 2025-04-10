from rest_framework import serializers
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзывов"""

    class Meta:
        model = Review
        fields = ['text', 'mark']  # Включаем все поля модели



class ProductListSerializer(serializers.Serializer):
    """Сериализатор для списка товаров"""
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
"""    class Meta:
        model = Product
        fields = '__all__'"""


class ProductDetailsSerializer(serializers.ModelSerializer):
    """Сериализатор для деталей товара"""
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']  # Добавляем поле reviews

