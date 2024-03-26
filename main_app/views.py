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
        pass
     
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
        queryset = Tags.objects.all()
        tags_serializer = TagsSerializer(queryset)
        print(tags_serializer.data)
        return JsonResponse(tags_serializer.data,
                            safe = False,
                            )


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