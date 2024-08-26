from django.contrib import admin

from .models import (Products,
                     Review,
                     Order,
                     Tags,
                     Categories,
                     Productavatar,
                     Categoriesavatar,
                     Subcategoriesavatar,
                     Subcategories,
                     BasketItems,
                     )


class ProductImageInline(admin.TabularInline):
    model = Products.images.through


class ProductInline(admin.TabularInline):
    model = Products


@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'image',
    ]


@admin.register(Subcategoriesavatar)
class Subcategoriesavatar(admin.ModelAdmin):

    list_display = [
        'src',
        'alt',
    ]


@admin.register(Categoriesavatar)
class CategoriesavatarAdmin(admin.ModelAdmin):

    list_display = [
        'src',
        'alt',
    ]


@admin.register(Productavatar)
class ProductavatarAdmin(admin.ModelAdmin):

    list_display = [
        'src',
        'alt',
    ]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):

    inlines = [
        ProductImageInline,
    ]

    list_display = [
        'title',
        'description',
        'fullDescription',
        'price',
        'producer',
        'date',
        'category',
        'freeDelivery',
        'dateFrom',
        'dateTo',
        'count',
        'available',
        'rating',
    ]

    exclude = [
        'images'
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = [
        'author',
        'email',
        'rate',
        'text',
        'date',
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = [
        'fullName',
        'email',
        'paymentType',
        'phone',
        'totalCost',
        'city',
        'address',
        'createdAt',
        'status',
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
        'image',
    ]


@admin.register(BasketItems)
class BasketItemAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'archived',
    ]
