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


class DeliveryTypeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = DeliveryType
        fields = [
            'name',
        ]

    def get_name(self, obj):
        print(obj)
        return str(obj.name)


class PaymentmethodSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Payment
        fields = [
            'name',
        ]

    def get_name(self, obj):
        print(obj)
        return str(obj)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'author',
            'email',
            'points',
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
    title = serializers.SerializerMethodField()

    class Meta:
        model = Subcategories
        fields = [
            'id',
            'title',
            'image',
        ]
        
    def get_title(self, obj):
        return obj.title


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
    images = ProductavatarSerializer(many = True)
    reviews = ReviewSerializer(many = True)
    
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
    images = ProductavatarSerializer()

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
    deliveryType = DeliveryTypeSerializer()
    paymentType = PaymentmethodSerializer()
    
    class Meta:
        model = Order
        fields = [
            'id',
            'createdAt',
            'fullName',
            'email',
            'phone',
            'deliveryType',
            'paymentType',
            'totalCost',
            'status',
            'city',
            'address',
            'products',
        ]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
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