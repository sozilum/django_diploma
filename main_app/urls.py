from .views import (ProductView,
                    BasketView,
                    OrderView,
                    )
from django.urls import path

urlpatterns = [
    path('categories/', ProductView.get_categories, name = 'categories'),
    # path('tags/', ProductView.get_tags, name = 'tags'),
]