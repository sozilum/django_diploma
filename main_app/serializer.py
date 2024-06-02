from rest_framework import serializers
from .models import (Product,
                    Order,
                    Payment,
                    Review,
                    Tags,
                    Categories,
                    DeliveryType,
                    Basket,
                    Subcategories,
                    Productavatar,
                    Categoriesavatar,
                    Subcategoriesavatar,
                    )


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


class SubcategoriesavatarSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = Subcategoriesavatar
        fields = [
            'src',
            'alt',
        ]

    def get_src(self, obj):
        return obj.src.url

class CategoriesavatarSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = Categoriesavatar
        fields = [
            'src',
            'alt',
        ]

    def get_src(self, obj):
        return obj.src.url

class ProductavatarSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = Productavatar
        fields = [
            'src',
            'alt',
        ]

    def get_src(self, obj):
        return obj.src.url


class SubcategoriesSerializer(serializers.ModelSerializer):
    image = SubcategoriesavatarSerializer()

    class Meta:
        model = Subcategories
        fields = [
            'id',
            'title',
            'image',
        ]

class CategoriesSerializer(serializers.ModelSerializer):
    subcategories = SubcategoriesSerializer()
    image = CategoriesavatarSerializer()
    
    class Meta:
        model = Categories
        fields = [
            'id',
            'title',
            'image',
            'subcategories',
        ]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductavatarSerializer()
    reviews = ReviewSerializer()
    
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
            'specifications',
            'category',
            'rating',
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
    products = ProductSerializer()

    class Meta:
        model = Basket
        fields = [
            'user',
            'products',
            'count',
        ]