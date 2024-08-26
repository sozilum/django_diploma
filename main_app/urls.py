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
                    ProductView,
                    ProductReviewView,
                    )
from django.urls import path

urlpatterns = [
    path('products/popular/', PopularProductView.as_view(), name='popular'),
    path('products/limited/', LimitedProductView.as_view(), name='limited'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('product/<int:id>/reviews/', ProductReviewView.as_view(), name='review'),

    path('categories/', CategoriesView.as_view(), name='categories'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('sales/', SalesProductView.as_view(), name='sales'),
    path('banners/', BannerView.as_view(), name='banner'),
    path('tags/', TagsView.as_view(), name='tags'),
    path('basket/', BasketView.as_view(), name='basket'),

    path('orders/', OrderView.as_view(), name='order'),
    path('order/<int:id>/', UserOrderView.as_view(), name='user_order'),

    path('payment/<int:id>/', PaymentView.as_view(), name='payment'),
]
