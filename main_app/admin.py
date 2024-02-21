from django.contrib import admin

from .models import (Product,
                     Review,
                     Payment,
                     Order,
                     Tags,
                     Categories,
                     DeliveryType,
                     )




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'image',
        'description',
        'price',
        'review',
        'producer',
        'date',
        'tags',
        'categories',
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = [
        'author',
        'points',
        'title',
        'review',
        'date',
    ]


@admin.register(Payment)
class PaymetAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = [
        'author',
        'products',
        'delivery_address',
        'delivery_type',
        'payment',
        'date'
    ]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]


@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]