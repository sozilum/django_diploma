from rest_framework.views import APIView

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

import json


class BannerView(APIView):
    def get_banner(self):
        queryset = Product.objects.all()[:1:]
        serializer_data = BannerSerializer(queryset,
                                           many = True,
                                           )
        
        data = serializer_data.data[0]

        new_list = [
            {
                'id':data['id'],
                'category':data['category'],
                'price':data['price'],
                'count':data['count'],
                'date':data['date'],
                'title':data['title'],
                'description':data['description'],
                'freeDelivery':data['freeDelivery'],
                'images':[{
                    'src':data['images'],
                    'alt':'',
                }
                    ],
                'tags':data['tags'],
                'reviews':data['reviews'],
                # 'rating':data['rating'],
            }
        ]
        return JsonResponse(data = new_list,
                            safe = False,
                            )


class CategoriesView(APIView):
    def get_categories(self):
        queryset = Categories.objects.all()
        serialized_data = CategoriesSerializer(queryset,
                                               many = True,
                                               )
        
        data = serialized_data.data
        new_list = []
        for index in range(len(data)):
            new_list.append(
                {
                    'id':data[index]['id'],
                    'title':data[index]['title'],
                    'image':[
                        {
                            'src':data[index]['image'],
                            'alt':'',
                        },
                    ],
                    'subcategories': [
                        {
                            'id':data[index]['id'],
                            'title':data[index]['title'],
                            'image':[
                                {
                                    'src':data[index]['image'],
                                    'alt':'',
                                },
                                ]
                        }
                    ],
                    
                }
            )

        return JsonResponse(data = new_list,
                            safe = False,
                            )

class CatalogView(APIView):
    def get_catalog(self):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )

        data = data_serializer.data
        new_list = []

        for index in range(len(data)):
            new_list.append(
                {
                    'id':data[index]['id'],
                    'category':data[index]['category'],
                    'price':data[index]['price'],
                    'count':data[index]['count'],
                    'date':data[index]['date'],
                    'title':data[index]['title'],
                    'description':data[index]['description'],
                    'freeDelivery':data[index]['freeDelivery'],
                    'images':[
                        {
                            'src':data[index]['images'],
                            'alt':'',
                            }
                        ],
                    'tags':data[index]['tags'],
                    'reviews':data[index]['reviews'],
                    # 'rating':data[index]['rating'],
                }
            )

        for i in new_list:
            print(i, '\n')
        return JsonResponse(data = new_list,
                            safe = False,
                            )

class PopularProductView(APIView):
    def get_products_popular(self):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )
        
        data = data_serializer.data
        new_list = []

        for index in range(len(data)):
            new_list.append(
                {
                    'id':data[index]['id'],
                    'category':data[index]['category'],
                    'price':data[index]['price'],
                    'count':data[index]['count'],
                    'date':data[index]['date'],
                    'title':data[index]['title'],
                    'description':data[index]['description'],
                    'freeDelivery':data[index]['freeDelivery'],
                    'images':[
                        {
                            'src':data[index]['images'],
                            'alt':'',
                            }
                        ],
                    'tags':data[index]['tags'],
                    'reviews':data[index]['reviews'],
                    # 'rating':data[index]['rating'],
                }
            )

        return JsonResponse(data = new_list,
                            safe = False,
                            )

class LimitedProductView(APIView):
    def get_products_limited(self):
        queryset = Product.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many = True,
                                            )
        
        data = data_serializer.data
        new_list = []

        for index in range(len(data)):
            new_list.append(
                {
                    'id':data[index]['id'],
                    'category':data[index]['category'],
                    'price':data[index]['price'],
                    'count':data[index]['count'],
                    'date':data[index]['date'],
                    'title':data[index]['title'],
                    'description':data[index]['description'],
                    'freeDelivery':data[index]['freeDelivery'],
                    'images':[
                        {
                            'src':data[index]['images'],
                            'alt':'',
                            }
                        ],
                    'tags':data[index]['tags'],
                    'reviews':data[index]['reviews'],
                    # 'rating':data[index]['rating'],
                }
            )

        return JsonResponse(data = new_list, 
                            safe=False,
                            )
    

class SalesProductView(APIView):
    def get_sales(self):
        queryset = Product.objects.all()
        data_serializer = SalesSerializer(queryset,
                                          many = True,
                                          )
        
        data = data_serializer.data
        new_list = []

        for index in range(len(data)):
            new_list.append(
                {
                    'id':data[index]['id'],
                    'price':data[index]['price'],
                    'salePrice':data[index]['salePrice'],
                    'dateFrom':data[index]['dateFrom'],
                    'dateTo':data[index]['dateTo'],
                    'title':data[index]['title'],
                    'images':[
                        {
                            'src':data[index]['images'],
                            'alt':'',
                            }
                        ],
                }
            )
        print(new_list)
        return JsonResponse(data = new_list,
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
    def get_basket(self):
        queryset = Basket.objects.filter(user_id = self.user.id)
        data_serializer = BasketSerializer(queryset,
                                           many = True,
                                           )
        basket_data = data_serializer.data[0]
        
        # print(data_serializer.data[0]['count'])

        product_queryset = Product.objects.filter(id = basket_data['products'])
        product_serializer = ProductSerializer(product_queryset,
                                               many = True,
                                               )
        data = product_serializer.data
        new_list = []
        for index in range(len(data)):
            new_list.append(
                {
                    'id':data[index]['id'],
                    'category':data[index]['category'],
                    'price':data[index]['price'],
                    'count':basket_data['count'],
                    'date':data[index]['date'],
                    'title':data[index]['title'],
                    'description':data[index]['description'],
                    'freeDelivery':data[index]['freeDelivery'],
                    'images':[
                        {
                            'src':data[index]['images'],
                            'alt':'',
                            }
                        ],
                    'tags':data[index]['tags'],
                    'reviews':data[index]['reviews'],
                    # 'rating':data[index]['rating'],
                }
            )
        return JsonResponse(data = new_list,
                            safe = False,
                            )
    

class UpdateBasketView(APIView):
    def post_basket(self):

        print('It works, POST')

        return HttpResponse(status = 200)
    

class DeleteBasketView(APIView):
    def delete_basket(self):
        
        print('It works, DELETE')

        return HttpResponse(status = 200)

class OrderView(APIView):
    def get_order(self):
        queryset = Order.objects.filter(fullName_id = self.user.id)
        serializer_data = OrderSerializer(queryset,
                                          many = True,
                                          )
        
        data = serializer_data.data
        new_list = []
        for index in range(len(data)):
            new_list.append(
                {
                    'fullName':data[index]['fullName'],
                    'email':data[index]['email'],
                    'phone':data[index]['phone'],
                    'paymentType':data[index]['paymentType'],
                    'totalCost':data[index]['totalCost'],
                    'city':data[index]['city'],
                    'products':data[index]['products'],
                    'address':data[index]['address'],
                    'fullName':data[index]['fullName'],
                    'deliveryType':data[index]['deliveryType'],
                    'createdAt':data[index]['createdAt'],
                    'status':data[index]['status'],
                }
            )

        print(new_list)

        return HttpResponse(status = 200)

class UpdateOrderView(APIView):
    def post_order(self):
        ...
        return HttpResponse(status = 200)

class UserOrderView(APIView):
    def get_user_order(self):
        ...
        return HttpResponse(status = 200)

class UserUpdateOrderView(APIView):
    def post_user_order(self):
        ...
        return HttpResponse(status = 200)

class PaymentView(APIView):
    def get_payment(self):
        ...
        return HttpResponse(status = 200)