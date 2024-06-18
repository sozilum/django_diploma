from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.urls import (reverse_lazy,
                         reverse,
                         )
from django.http import (HttpResponse,
                         JsonResponse,
                         HttpResponseRedirect,
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
        # data = categories_crutch(serialized_data.data) ?
        return JsonResponse(data = serialized_data.data,
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
        # 'Need a photo to be visible on page!'
        # data = sales_crutch(data_serializer.data)

        return JsonResponse(data = {'items':data_serializer.data})



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
        for data_index in data_serializer.data:
            product_query = Product.objects.filter(id = data_index['products'])
            product_serializer = ProductSerializer(product_query,
                                                   many = True,
                                                   )
            product_serializer.data[0]['count'] = data_index['count']
            new_list.append(product_serializer.data[0])
            
        return JsonResponse(data = new_list,
                            safe = False,
                            )
    
    
    def post(self, request):
        queryset = Basket.objects.filter(user_id = request.user.id,
                                         products_id = request.data['id']
                                         )
        data_serializer = BasketSerializer(queryset,
                                           many = True,
                                           )
        queryset.update(count = data_serializer.data[0]['count'] + request.data['count'])
        return HttpResponseRedirect(redirect_to = reverse_lazy('basket'))
    

    def delete(self, request):
        data = json.loads(request.body)
        queryset = Basket.objects.filter(user_id = request.user.id,
                                         products_id = data['id']
                                         )
        data_serializer = BasketSerializer(queryset,
                                           many = True,
                                           )
        
        if data_serializer.data[0]['count'] - data['count'] != 0:
            queryset.update(count = data_serializer.data[0]['count'] - data['count'])
        
        else:
            queryset.delete()
        
        # return HttpResponseRedirect(redirect_to = reverse_lazy('basket')) looping...
        return HttpResponse(status = 200)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    #history-order - actual page

    def get(self, request):
        queryset = Order.objects.filter(fullName_id = request.user.id)
        data_serializer = OrderSerializer(queryset,
                                          many = True,
                                          )
        
        
        # data = order_crutch(serializer_data.data)
        print(request.data, 'Its OrderView Get request')
        
        return JsonResponse(data = data_serializer.data,
                            safe = False,
                            )

    def post(self, request):
        print(request.data, 'Its OrderView POST request')
        
        queryset = Order.objects.filter(fullName_id = request.user.id,
                                        status = True,
                                        )
        
        return HttpResponse(status = 200)


class UserOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        queryset = Order.objects.filter(fullName = request.user.id,
                                        id = id,
                                        )
        data_serializer = OrderSerializer(queryset,
                                          many = True,
                                          )        
        
        print('Its UserOrderView, GET request')
        return JsonResponse(data = data_serializer.data,
                            safe = False,
                            )

    def post(self, request, id):
        print('its UserOrderView, POST request')
        return HttpResponse(status = 200)


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print('Its paymetnview, GET request')
        return HttpResponse(status = 200)