from rest_framework import serializers
from .models import (Product,
                    Order,
                    Payment,
                    Review,
                    Tags,
                    Categories,
                    DeliveryType,
                    )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'full_description',
            'price',
            'review',
            'date',
            'tags',
            'categories',
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'author',
            'products',
            'delivery_address',
            'delivery_type',
            'payment',
            'date',
            'free_delivery',
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'author',
            'email',
            'points',
            'title',
            'text',
            'date',
        ]


class PaymentmethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'name',
        ]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = [
            'name',
        ]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = [
            'title',
        ]

class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = [
            'name',
        ]