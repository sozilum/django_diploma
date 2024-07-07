import pathlib

def userorderview(self):
    new_list = []
    for product in self['baskets']:
        product['products']['count'] = product['count']
        new_list.append(product['products'])


    data = {
        "id": self['id'],
        "createdAt": self['createdAt'],
        "fullName": self['fullName'],
        "email": self['email'],
        "phone": self['phone'],
        "deliveryType": self['deliveryType'],
        "paymentType": self['paymentType'],
        "totalCost": self['totalCost'],
        "status": self['status'],
        "city": self['city'],
        "address": self['address'],
        "products": new_list,
    }
    return data



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