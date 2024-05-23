from .views import (CategoriesView,
                    CatalogView,
                    PopularProductView,
                    LimitedProductView,
                    SalesProductView,
                    BannerView,
                    TagsView,
                    BasketView,
                    OrderView,
                    UserOrderView,
                    PaymentView,
                    )
from django.urls import path

urlpatterns = [
    path('categories/', CategoriesView.get_categories, name = 'categories'),
    path('catalog/', CatalogView.get_catalog, name = 'catalog'),
    path('products/popular/', PopularProductView.get_products_popular, name = 'popular'),
    path('products/limited/', LimitedProductView.get_products_limited, name = 'limited'),
    path('sales/', SalesProductView.get_sales, name = 'sales'),
    path('banners/', BannerView.get_banner, name = 'banner'),
    path('tags/', TagsView.get_tags, name = 'tags'),

    path('basket/', BasketView.as_view(), name = 'basket'),

    path('orders/', OrderView.as_view(), name = 'order'),

    path('orders/{id}/', UserOrderView.as_view(), name = 'user_order'),

    path('payment/', PaymentView.get_payment, name = 'payment'),
]