


def categories_crutch(data) ->list:
    new_list = []

    for index in data:
        new_list.append(
            {
                'id':index['id'],
                'title':index['title'],
                'image':[
                    {
                        'src':index['image']['src'],
                        'alt':index['image']['alt'],
                    },
                    ],
                'subcategories':[
                    {
                        'id':index['subcategories']['id'],
                        'title':index['subcategories']['title'],
                        'image':[
                            {
                                'src':index['subcategories']['image']['src'],
                                'alt':index['subcategories']['image']['alt'],
                                },
                            ],
                        },
                    ],
                },
            ),
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