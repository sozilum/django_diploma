from rest_framework import serializers
from .models import (Product,
                    Order,
                    Payment,
                    Review,
                    Tags,
                    Categories,
                    DeliveryType,
                    Basket,
                    )


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'price',
            'count',
            'date',
            'title',
            'description',
            'freeDelivery',
            'images',
            'tags',
            'reviews',
            'rating',

        ]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = [
            'id',
            'title',
            'image',
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'price',
            'count',
            'date',
            'title',
            'description',
            'fullDescription',
            'freeDelivery',
            'images',
            'tags',
            'reviews',
            'category',
        ]


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'price',
            'salePrice',
            'dateFrom',
            'dateTo',
            'title',
            'images',
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'fullName',
            'email',
            'phone',
            'paymentType',
            'totalCost',
            'city',
            'products',
            'address',
            'deliveryType',
            'createdAt',
            'status',
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



class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = [
            'name',
        ]


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'user',
            'products',
            'count',
        ]