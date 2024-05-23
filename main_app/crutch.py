


def product_crutch(data) -> list:
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
        return new_list


def banner_crutch(data) -> list:
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
        return new_list


def categories_crutch(data) ->list:
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
    return new_list


def sales_crutch(data) -> list:
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
    return new_list


def order_crutch(data) -> list:
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
    return new_list


def user_product_crutch(data) -> list:
    ...