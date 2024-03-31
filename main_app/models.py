from django.contrib.auth.models import User
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

def image_upload_categories(instance:'Categories', filename:str) -> str:
    return 'categories/category_{pk}/{filename}'.format(pk = instance.pk,
                                                        filename = filename
                                                        )


class Categories(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = image_upload_categories,
                              null = True,
                              )

    def __str__(self) -> str:
        return self.title


class Payment(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class DeliveryType(models.Model):
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
            'title',
            'price',
            'producer',
        ]

    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = image_upload,
                              null = True,
                              )
    description = models.CharField(max_length = 100,
                                   null = True,
                                   )
    full_description = models.TextField(null = True)
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
    free_delivery = models.BooleanField(default = False)
    available = models.BooleanField(default = True)

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
    points = models.DecimalField(max_digits = 1,
                                 decimal_places = 1,
                                 null = True,
                                 )
    text = models.TextField(null = True)
    date = models.DateTimeField(auto_now_add = True)
    product = models.OneToOneField(to = Product,
                                   on_delete = models.CASCADE,
                                   null = True,
                                   blank = True,
                                   )
    

class Order(models.Model):
    class Meta:
        ordering = [
            'date',
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
    free_delivery = models.BooleanField(order_free_delivery)