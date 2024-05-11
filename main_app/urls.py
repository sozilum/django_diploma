from .views import (CategoriesView,
                    CatalogView,
                    PopularProductView,
                    LimitedProductView,
                    SalesProductView,
                    BannerView,
                    TagsView,
                    BasketView,
                    # UpdateBasketView,
                    # DeleteBasketView,
                    OrderView,
                    UpdateOrderView,
                    UserOrderView,
                    UserUpdateOrderView,
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

    path('basket/', BasketView.get, name = 'basket'),
    path('basket/', BasketView.post, name = 'update_basket'),
    path('basket/', BasketView.delete, name = 'delete'),

    path('orders/', OrderView.get_order, name = 'order'),
    path('orders/', UpdateOrderView.post_order, name = 'update_order'),
    
    path('orders/{id}/', UserOrderView.get_user_order, name = 'user_order'),
    path('orders/{id}/', UserUpdateOrderView.post_user_order, name = 'update_user_order'),

    path('payment/', PaymentView.get_payment, name = 'payment'),
]