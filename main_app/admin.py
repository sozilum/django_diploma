from django.contrib import admin

from .models import (Product,
                     Review,
                     Payment,
                     Order,
                     Tags,
                     Categories,
                     DeliveryType,
                     Basket,
                     Productavatar,
                     Categoriesavatar,
                     Subcategoriesavatar,
                     Subcategories,
                     )

class ProductImageInline(admin.TabularInline):
    model = Product.images.through


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


@admin.register(Product)
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
        'tags',
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
        'points',
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
        'subcategories',
    ]


@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        # 'count',
    ]