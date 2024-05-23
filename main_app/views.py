from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.http import (HttpResponse,
                         JsonResponse,
                         )
from .models import (Product,
                     Categories,
                     Tags,
                     Order,
                     Basket,
                     )

from .serializer import (BannerSerializer,
                         CategoriesSerializer,
                         ProductSerializer,
                         SalesSerializer,
                         TagsSerializer,
                         OrderSerializer,
                         BasketSerializer,
                         )

from .crutch import (product_crutch,
                     banner_crutch,
                     categories_crutch,
                     sales_crutch,
                     order_crutch,
                     user_product_crutch,
                     )

import json


class BannerView(APIView):
    def get_banner(self):
        queryset = Product.objects.all()[:1:]
        serializer_data = BannerSerializer(queryset,
                                           many = True,
                                           )
        
        data = banner_crutch(serializer_data.data[0])

        return JsonResponse(data = data,
                            safe = False,
                            )


class CategoriesView(APIView):
    def get_categories(self):
        queryset = Categories.objects.all()
        serialized_data = CategoriesSerializer(queryset,
                                               many = True,
                                               )
        
        data = categories_crutch(serialized_data.data)

        return JsonResponse(data = data,
                            safe = False,
                            )

class CatalogView(APIView):
    def get_catalog(self):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )

        data = product_crutch(data_serializer.data)

        return JsonResponse(data = data,
                            safe = False,
                            )

class PopularProductView(APIView):
    def get_products_popular(self):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )
        
        data = product_crutch(data_serializer.data)

        return JsonResponse(data = data,
                            safe = False,
                            )


class LimitedProductView(APIView):
    def get_products_limited(self):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )
        
        data = product_crutch(data_serializer.data)

        return JsonResponse(data = data, 
                            safe=False,
                            )
    

class SalesProductView(APIView):
    def get_sales(self):
        queryset = Product.objects.all()
        data_serializer = SalesSerializer(queryset,
                                          many = True,
                                          )
        
        data = sales_crutch(data_serializer.data)

        return JsonResponse(data = data,
                            safe = False,
                            )


class TagsView(APIView):
    def get_tags(self):
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
        for index in range(len(data_serializer.data)):

            basket_data = data_serializer.data[index]
            
            product_queryset = Product.objects.filter(id = basket_data['products'])
            product_serializer = ProductSerializer(product_queryset,
                                                   many = True,
                                                   )
            data = product_serializer.data[0]
            
            new_list.append(
                {
                    'id':data['id'],
                    'category':data['category'],
                    'price':data['price'],
                    'count':basket_data['count'],
                    'date':data['date'],
                    'title':data['title'],
                    'description':data['description'],
                    'freeDelivery':data['freeDelivery'],
                    'images':[
                        {
                            'src':data['images'],
                            'alt':'',
                            }
                        ],
                    'tags':data['tags'],
                    'reviews':data['reviews'],
                    # 'rating':data['rating'],
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
        
        return JsonResponse()


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
    def get_payment(self):
        ...
        return HttpResponse(status = 200)