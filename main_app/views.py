from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http import (HttpResponse,
                         JsonResponse,
                         )
from .models import (Products,
                     Categories,
                     Tags,
                     Order,
                     BasketItems,
                     )

from .serializer import (CategoriesSerializer,
                         ProductSerializer,
                         SalesSerializer,
                         TagsSerializer,
                         OrderSerializer,
                         BasketItemSerializer,
                         ReviewSerializer,
                         )

from .crutch import (userorderview)

import json


class BannerView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Products.objects.all()
        serializer_data = ProductSerializer(queryset,
                                            many=True,
                                            )
        return JsonResponse(data=serializer_data.data,
                            safe=False,
                            )


class ProductView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        queryset = Products.objects.filter(id=id)
        data_serializer = ProductSerializer(queryset,
                                            many=True,
                                            )
        return JsonResponse(data=data_serializer.data[0])


class ProductReviewView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        queryset = Products.objects.filter(id=id)
        data_serializer = ProductSerializer(queryset,
                                            many=True,
                                            )
        reviews = data_serializer.data[0]['reviews']
        return JsonResponse(data=reviews,
                            safe=False,
                            )

    def post(self, request, id):
        queryset = Products.objects.filter(id=id)
        for data in queryset:
            data.reviews.create(author=request.data['author'],
                                email=request.data['email'],
                                text=request.data['text'],
                                rate=request.data['rate'],
                                )
        num = 0
        for data in queryset:
            reviews_data = data.reviews.all()

            serializer_data = ReviewSerializer(reviews_data,
                                               many=True,
                                               )

            for inner_data in serializer_data.data:
                num += inner_data['rate']

            num //= len(serializer_data.data)
            queryset.update(rating=num)

        return HttpResponse(status=200)


class CategoriesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Categories.objects.all()
        serializer_data = CategoriesSerializer(queryset,
                                               many=True,
                                               )
        return JsonResponse(data=serializer_data.data,
                            safe=False,
                            )


class CatalogView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Products.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many=True,
                                            )
        data = {'items': data_serializer.data}
        return JsonResponse(data=data)


class PopularProductView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Products.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many=True,
                                            )
        return JsonResponse(data=data_serializer.data,
                            safe=False,
                            )


class LimitedProductView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Products.objects.all()
        data_serializer = ProductSerializer(queryset,
                                            many=True,
                                            )
        return JsonResponse(data=data_serializer.data,
                            safe=False,
                            )


class SalesProductView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Products.objects.all()
        data_serializer = SalesSerializer(queryset,
                                          many=True,
                                          )
        data = {'items': data_serializer.data}
        return JsonResponse(data=data)


class TagsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Tags.objects.all()
        data_serializer = TagsSerializer(queryset,
                                         many=True,
                                         )
        return JsonResponse(data=data_serializer.data,
                            safe=False,
                            )


class BasketView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = BasketItems.objects.filter(user_id=request.user.id,
                                              archived=False,
                                              )
        data_serializer = BasketItemSerializer(queryset,
                                               many=True,
                                               )
        new_list = []
        for data_index in data_serializer.data:
            data_index['products']['count'] = data_index['count']
            new_list.append(data_index['products'])

        return JsonResponse(data=new_list,
                            safe=False,
                            )

    def post(self, request):
        queryset = BasketItems.objects.filter(user_id=request.user.id,
                                              archived=False,
                                              products_id=request.data['id']
                                              )
        data_serializer = BasketItemSerializer(queryset,
                                               many=True,
                                               )
        try:
            queryset.update(
                count=data_serializer.data[0]['count'] +
                request.data['count'])

        except BaseException:
            queryset.create(count=request.data['count'],
                            user_id=request.user.id,
                            products_id=request.data['id'],
                            )

        return HttpResponse(status=200)

    def delete(self, request):
        data = json.loads(request.body)
        queryset = BasketItems.objects.filter(user_id=request.user.id,
                                              products_id=data['id'],
                                              archived=False,
                                              )
        data_serializer = BasketItemSerializer(queryset,
                                               many=True,
                                               )
        count = data_serializer.data[0]['count']
        if data['count'] == count:
            queryset.delete()

        else:
            queryset.update(count=count - data['count'])
        return HttpResponse(status=200)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Order.objects.filter(fullName_id=request.user.id,
                                        )
        data_serializer = OrderSerializer(queryset,
                                          many=True,
                                          )
        return JsonResponse(data=data_serializer.data,
                            safe=False,
                            )

    def post(self, request):
        basket_query = BasketItems.objects.filter(user_id=request.user.id,
                                                  archived=False,
                                                  )
        num = 0
        for basket_data in request.data:
            num += float(basket_data['count']) * float(basket_data['price'])

        Order.objects.update_or_create(fullName_id=request.user.id,
                                       status=True,
                                       totalCost=num,
                                       )
        order_query = Order.objects.filter(fullName_id=request.user.id,
                                           status=True,
                                           )
        for order in order_query:
            order.baskets.set(basket_query)

        data_serializer = OrderSerializer(order_query,
                                          many=True,
                                          )
        data = {'orderId': data_serializer.data[0]['id']}
        return JsonResponse(data)


class UserOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        queryset = Order.objects.filter(fullName=request.user.id,
                                        status=True,
                                        id=id,
                                        )
        data_serializer = OrderSerializer(queryset,
                                          many=True,
                                          )
        data = userorderview(data_serializer.data[0])
        return JsonResponse(data=data)

    def post(self, request, id):
        queryset = Order.objects.filter(fullName=request.user.id,
                                        status=True,
                                        id=id,
                                        )
        queryset.update(email=request.data['email'],
                        phone=request.data['phone'],
                        city=request.data['city'],
                        address=request.data['address'],
                        deliveryType=request.data['deliveryType'],
                        paymentType=request.data['paymentType'],
                        )
        data_serialzier = OrderSerializer(queryset,
                                          many=True,
                                          )

        data = {'orderId': data_serialzier.data[0]['id']}
        return JsonResponse(data=data)


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        return HttpResponse(status=200)

    def post(self, request, id):
        basket_query = BasketItems.objects.filter(user_id=request.user.id,
                                                  archived=False,
                                                  )
        basket_query.update(archived=True)
        return HttpResponse(status=200)
