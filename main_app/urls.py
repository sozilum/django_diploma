from .views import (ProductView,
                    CategoriesView,
                    TagsView,
                    BasketView,
                    )

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'catalog',
                ProductView,
                )
router.register(r'categories',
                CategoriesView,
                )
router.register(r'tags',
                TagsView,
                )
router.register(r'basket',
                BasketView,
                )

urlpatterns = router.urls