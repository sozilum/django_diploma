from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

def image_upload(instance:'Product', filename: str) -> str:
    return 'products/product_{pk}/{filename}'.format(pk = instance.pk,
                                                    filename = filename,
                                                    )
def order_free_delivery(self):
    price = 0
    for product in self.products:
        price += product.price

    if price >= 2000:
        return True
    
    else:
        return False

def user_email(self):
    return self.user.email

def user_phone(self):
    return self.user.phone

def user_fullname(self):
    return self.user.fullName

def total_cost(self):
    cost = int()
    for i_product in self.order.products:
        if i_product['salePrice'] > 0:
            cost += i_product['salePrice']
        else:
            cost += i_product['price']
    
    return cost

def image_upload_categories(instance:'Categories', filename:str) -> str:
    return 'categories/category_{pk}/{filename}'.format(pk = instance.pk,
                                                        filename = filename
                                                        )

def avg_rating(self):
    if self.reviews.points:
        return [index for index in self.reviews.points] // len(self.reviews.points)
    
    else:
        return 0


class Categories(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = image_upload_categories,
                              null = True,
                              )

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    class Meta:
        ordering = [
            'date',
            'points',
        ]

    author = models.OneToOneField(User,
                                  on_delete = models.CASCADE,
                                  null = True,
                                  )
    email = models.TextField(user_email,
                             null = True,
                             )
    points = models.PositiveSmallIntegerField(null = True)
    text = models.TextField(null = True)
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.email


class Payment(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class DeliveryType(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self) -> str:
        return self.name

class Specifications(models.Model):
    name = models.CharField(max_length = 50)
    value = models.TextField()

class Tags(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    class Meta:
        ordering = [
            'title',
            'price',
            'producer',
        ]

    title = models.CharField(max_length = 100)
    images = models.ImageField(upload_to = image_upload,
                              null = True,
                              )
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
    tags = models.ForeignKey(Tags,
                             on_delete = models.CASCADE,
                             null = True,
                             )
    category = models.ForeignKey(Categories,
                                   on_delete = models.CASCADE,
                                   null = True,
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
                                       on_delete = models.CASCADE,
                                       null = True,
                                       blank = True,
                                       )
    reviews = models.ForeignKey(Review,
                                on_delete = models.CASCADE,
                                null = True,
                                blank = True,
                                )
    rating = models.TextField(avg_rating,
                              null = True,
                              blank = True,
                              )
    def __str__(self) -> str:
        return self.title


class Basket(models.Model):
    class Meta:
        ordering = [
            'products',
        ]
    
    user = models.OneToOneField(User,
                                on_delete = models.CASCADE,
                                )
    products = models.ForeignKey(Product,
                                 on_delete = models.CASCADE,
                                 null = True,
                                 blank = True,
                                 )
    count = models.PositiveSmallIntegerField(default = 0,
                                             null = True,
                                             blank = True,
                                             )
    
    
    def __str__(self) -> str:
        return str(self.user)


class Order(models.Model):
    class Meta:
        ordering = [
            'createdAt',
            ]

    fullName = models.OneToOneField(User,
                                    on_delete = models.CASCADE,
                                    null = True,
                                    )
    email = models.TextField(user_email,
                             default = None,
                             null = True,
                             )
    phone = models.TextField(user_phone,
                             default = None,
                             null = True,
                             )
    paymentType = models.ForeignKey(Payment,
                                    on_delete = models.CASCADE,
                                    null = True,
                                    )
    totalCost = models.TextField(total_cost,
                                 default = 0,
                                 )
    city = models.TextField(max_length = 50,
                            default = None,
                            null = True,
                            )
    products = models.ForeignKey(Product,
                                 on_delete = models.CASCADE,
                                 null = True,   
                                 )
    address = models.CharField(max_length = 100)
    deliveryType = models.OneToOneField(DeliveryType,
                                        on_delete = models.CASCADE,
                                        null = True,
                                        )
    createdAt = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField(default = True)

    def __str__(self) -> str:
        return str(self.products)