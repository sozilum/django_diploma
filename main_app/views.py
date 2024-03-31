from rest_framework.views import APIView
from django.http import (HttpResponse,
                         JsonResponse,
                         )
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


class ProductView(APIView):
    def get_categories(self):
        queryset = Categories.objects.all()
        print(queryset)
        serialized_data = CategoriesSerializer(queryset)
        print(serialized_data)
        return JsonResponse(data = serialized_data.data,
                            safe = False,
                            )

    def get_catalog(self):
        pass

    def get_products_popular(self):
        pass

    def get_products_limited(self):
        pass

    def get_sales(self):
        pass

    def get_banner(self):
        pass

    def get_tags(self):
        pass


class BasketView(APIView):
    def get_basket(self):
        pass

    def post_basket(self):
        pass

    def delete_basket(self):
        pass


class OrderView(APIView):
    def get_order(self):
        pass

    def post_order(self):
        pass

    def get_user_order(self):
        pass

    def post_user_order(self):
        pass


class PaymentView(APIView):
    def get_payment(self):
        pass