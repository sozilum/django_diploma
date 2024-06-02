from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http import (HttpResponse,
                         JsonResponse,
                         )
from .models import (Product,
                     Categories,
                     Tags,
                     Order,
                     Basket,
                     )

from .serializer import (CategoriesSerializer,
                         ProductSerializer,
                         SalesSerializer,
                         TagsSerializer,
                         OrderSerializer,
                         BasketSerializer,
                         )

from .crutch import (order_crutch,
                     user_product_crutch,
                     categories_crutch,
                     )

import json


class BannerView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Product.objects.all()
        serializer_data = ProductSerializer(queryset,
                                            many = True,
                                            )
        return JsonResponse(data = serializer_data.data,
                            safe = False,
                            )


class CategoriesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Categories.objects.all()
        serialized_data = CategoriesSerializer(queryset,
                                               many = True,
                                               )
        data = categories_crutch(serialized_data.data)
        return JsonResponse(data = data,
                            safe = False,
                            )

class CatalogView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )
        return JsonResponse(data = data_serializer.data,
                            safe = False,
                            )


class PopularProductView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )
        return JsonResponse(data = data_serializer.data,
                            safe = False,
                            )


class LimitedProductView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )
        return JsonResponse(data = data_serializer.data,
                            safe=False,
                            )
    

class SalesProductView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Product.objects.all()
        data_serializer = SalesSerializer(queryset,
                                          many = True,
                                          )
        print('its doesnt work, correctly')
        return JsonResponse(data = data_serializer.data,
                            safe = False,
                            )


class TagsView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        queryset = Tags.objects.all()
        data_serializer = TagsSerializer(queryset,
                                         many = True,
                                         )
        return JsonResponse(data = data_serializer.data,
                            safe = False,
                            )


class BasketView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        queryset = Basket.objects.filter(user_id = request.user.id)
        data_serializer = BasketSerializer(queryset,
                                           many = True,
                                           )
        
        new_list = []
        for data in data_serializer.data:
            new_list.append(
                {
                    'id':data['products']['id'],
                    'category':data['products']['category'],
                    'price':data['products']['price'],
                    'count':data['count'],
                    'date':data['products']['date'],
                    'title':data['products']['title'],
                    'description':data['products']['description'],
                    'freeDelivery':data['products']['freeDelivery'],
                    'images':[
                        {
                            'src':data['products']['images']['src'],
                            'alt':data['products']['images']['alt'],
                            }
                        ],
                    'tags':data['products']['tags'],
                    'reviews':data['products']['reviews'],
                    # 'rating':data['products']['rating'],
                }
            )
        return JsonResponse(data = new_list,
                            safe = False,
                            )
    
    def post(self, request):
        print(request.POST)
        print('works, post?')
        return HttpResponse(status = 200)
    

    def delete(self, request):
        body = json.loads(request.body)
        queryset = Basket.objects.filter(user_id = request.user.id,
                                         products_id = body['id'],
                                         )
        serializer_data = BasketSerializer(queryset,
                                           many = True,
                                           )

        if serializer_data.data[0]['count'] == body['count']:
            queryset.delete()

        else:
            num = serializer_data.data[0]['count'] - body['count']
            queryset.update(count = num)
        
        return HttpResponse(status = 200)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        queryset = Order.objects.filter(fullName_id = request.user.id)
        serializer_data = OrderSerializer(queryset,
                                          many = True,
                                          )
        
        data = order_crutch(serializer_data.data)

        return JsonResponse(data = data,
                            safe = False,
                            )

    def post(self, request):
        print(request.POST)
        print('post is work?')
        return HttpResponse(status = 200)


class UserOrderView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, id):
        ...
        return HttpResponse(status = 200)

    def post(self, request, id):
        ...
        return HttpResponse(status = 200)


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self):
        ...
        return HttpResponse(status = 200)