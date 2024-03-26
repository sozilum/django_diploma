from .views import (ProductView,
                    BasketView,
                    OrderView,
                    )
from django.urls import path

urlpatterns = [
    path('tags/', ProductView.get_tags, name = 'tags'),
]