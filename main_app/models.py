from django.contrib.auth.models import User
from django.db import models

def image_upload(instance:'Product', filename: str) -> str:
    return 'products/product_{pk}/{filename}'.format(pk = instance.pk,
                                                    filename = filename,
                                                    )


class Payment(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name

class DeliveryType(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self) -> str:
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    class Meta:
        ordering = [
            'name',
            'price',
            'producer',
        ]

    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = image_upload,
                              null = True,
                              )
    description = models.TextField()
    price = models.DecimalField(max_digits = 10,
                                decimal_places = 2,
                                )
    producer = models.CharField(max_length = 100,
                                null = True,
                                )
    date = models.DateTimeField(auto_now_add = True)
    tags = models.ForeignKey(Tags,
                             on_delete = models.CASCADE,
                             null = True,
                             )
    categories = models.ForeignKey(Categories,
                                   on_delete = models.CASCADE,
                                   null = True,
                                   )
    def __str__(self) -> str:
        return self.name
    

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
    points = models.DecimalField(max_digits = 1,
                                 decimal_places = 1,
                                 null = True,
                                 )
    title = models.CharField(max_length = 100,
                             null = True,
                             )
    review = models.TextField(null = True)
    date = models.DateTimeField(auto_now_add = True)
    product = models.OneToOneField(to = Product,
                                   on_delete = models.CASCADE,
                                   null = True,
                                   blank = True,
                                   )
    

class Order(models.Model):
    class Meta:
        ordering = [
            'date'
            ]

    author = models.OneToOneField(User,
                                  on_delete = models.CASCADE,
                                  null = True,
                                  )
    products = models.ForeignKey(Product,
                                 on_delete = models.CASCADE,
                                 null = True,
                                 )
    delivery_address = models.CharField(max_length = 100)
    delivery_type = models.OneToOneField(DeliveryType,
                                         on_delete = models.CASCADE,
                                         null = True,
                                         )
    payment = models.OneToOneField(Payment,
                                   on_delete = models.CASCADE,
                                   null = True,
                                   )
    date = models.DateTimeField(auto_now_add = True)
    in_order = models.BooleanField(default = True) #Если заказ ещё не оплачен то будет отображатся в корзине

    def total_price(self):
        return sum(self.products.price)