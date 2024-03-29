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
        'title',
        'image',
        'full_description',
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
        'email',
        'text',
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
        'date',
        'in_order',
        'free_delivery',
    ]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    list_display = [
        'title',
    ]


@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]