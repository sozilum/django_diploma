from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models



def image_upload(instance:'Products' , filename: str) -> str:
    return 'products/{filename}'.format(filename = filename)

def image_upload_categories(instance:'Categories', filename:str) -> str:
    return 'categories/{filename}'.format(filename = filename)

def image_upload_subcategories(instance:'Subcategories', filename:str) -> str:
    return 'subcategories/{filename}'.format(filename = filename)

# Бесполезный кусок кода...
def order_free_delivery(self):
    price = 0
    for product in self.products:
        price += product.price

    if price >= 2000:
        return True
    
    else:
        return False

def avg_rating(self):
    if self.reviews.points:
        return [index for index in self.reviews.points] // len(self.reviews.points)
    
    else:
        return 0
    

def total_cost(self):
    cost = int()
    for i_product in self.order.products:
        if i_product['salePrice'] > 0:
            cost += i_product['salePrice']
        else:
            cost += i_product['price']
    
    return cost


def user_email(self):
    return self.user.email

def user_phone(self):
    return self.user.phone

def user_fullname(self):
    return self.user.fullName



class Subcategoriesavatar(models.Model):
    src = models.ImageField(upload_to = image_upload_subcategories,
                            null = True,
                            )
    alt = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.alt

class Categoriesavatar(models.Model):
    src = models.ImageField(upload_to = image_upload_categories,
                            null = True,
                            )
    alt = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.alt

class Productavatar(models.Model):
    src = models.ImageField(upload_to = image_upload,
                            null = True,
                            )
    alt = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.alt
    

class Subcategories(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ForeignKey(Subcategoriesavatar,
                              on_delete = models.PROTECT,
                              null = True,
                              )
    
    def __str__(self) -> str:
        return self.title

class Categories(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ForeignKey(Categoriesavatar,
                              on_delete = models.PROTECT,
                              null = True,
                              )
    subcategories = models.ManyToManyField(Subcategories)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    class Meta:
        ordering = [
            'date',
            'rate',
        ]

    author = models.CharField(blank = True,
                              null = True,
                              max_length = 100,
                              )
    email = models.TextField(blank = True,
                             null = True,
                             )
    rate = models.PositiveSmallIntegerField(null = True)
    text = models.TextField(null = True)
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.email


class Specifications(models.Model):
    name = models.CharField(max_length = 50)
    value = models.TextField()

    def __str__(self) -> str:
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    class Meta:
        ordering = [
            'title',
            'producer',
        ]

    title = models.CharField(max_length = 100)
    images = models.ManyToManyField(Productavatar)
    description = models.CharField(max_length = 100,
                                   null = True,
                                   )
    fullDescription = models.TextField(null = True,
                                        blank = True,
                                        )
    price = models.DecimalField(max_digits = 10,
                                decimal_places = 2,
                                )
    salePrice = models.DecimalField(max_digits = 10,
                                    decimal_places = 2,
                                    null = True,
                                    blank = True,
                                    )
    producer = models.CharField(max_length = 100,
                                null = True,
                                )
    date = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField(Tags)
    category = models.ForeignKey(Categories,
                                 on_delete = models.SET_NULL,
                                 null = True,
                                 blank = True,
                                 )
    freeDelivery = models.BooleanField(default = False)
    dateFrom = models.DateField(null = True,
                                default = None,
                                blank = True,
                                )
    dateTo = models.DateField(null = True,
                              default = None,
                              blank = True,
                              )
    count = models.IntegerField(default=0, null=True)
    available = models.BooleanField(null = True,
                                    default = 0,
                                    )
    specifications = models.ForeignKey(Specifications,
                                       on_delete = models.PROTECT,
                                       null = True,
                                       blank = True,
                                       )
    reviews = models.ManyToManyField(Review,
                                     blank = True,
                                     )
    rating = models.PositiveSmallIntegerField(blank = True,
                                              null = True,
                                              )
    
    def __str__(self) -> str:
        return self.title


class BasketItems(models.Model):
    class Meta:
        pass

    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE,
                             )
    products = models.ForeignKey(Products,
                                 on_delete = models.PROTECT,
                                 blank = True,
                                 )
    count = models.PositiveIntegerField(default = 0)
    archived = models.BooleanField(default = 0)

    def __str__(self) -> str:
        return '{}, {}'.format(self.user, self.products)


class Order(models.Model):
    class Meta:
        ordering = [
            'createdAt',
            ]

    fullName = models.ForeignKey(User,
                                 on_delete = models.CASCADE,
                                 null = True,
                                 )
    email = models.TextField(default = None,
                             blank = True,
                             null = True,
                             )
    phone = models.TextField(default = None,
                             blank = True,
                             null = True,
                             )
    paymentType = models.CharField(max_length = 50,
                                   null = True,
                                   blank = True,
                                   )
    totalCost = models.PositiveSmallIntegerField(default = 0)
    city = models.TextField(max_length = 50,
                            default = None,
                            blank = True,
                            null = True,
                            )
    baskets = models.ManyToManyField(BasketItems)
    address = models.CharField(max_length = 100,
                               blank = True,
                               null = True,
                               )
    deliveryType = models.CharField(max_length = 50,
                                    null = True,
                                    blank = True,
                                    )
    createdAt = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField(default = True)

    def __str__(self) -> str:
        return '{}, {}'.format(self.fullName, self.baskets)