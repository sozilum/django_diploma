from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from .models import (Product,
                     Categories,
                     Tags,
                     Order,
                     )

from .serializer import (ProductSerializer,
                         CategoriesSerializer,
                         TagsSerializer,
                         OrderSerializer,
                         )


class ProductView(viewsets.ReadOnlyModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

class TagsView(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class BasketView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer