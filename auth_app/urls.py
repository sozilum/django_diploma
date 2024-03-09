from rest_framework.routers import SimpleRouter
from .views import (SignUpView,
                    # SignInView,
                    # LogoutView,
                    )


router = SimpleRouter()
router.register(r'sign-up',
                SignUpView,
                basename='sing-up',
                )
urlpatterns = router.urls
# router.register(r'sign-in',
#                 SignInView,
#                 basename = 'login',
#                 )
# router.register(r'logout',
#                 LogoutView,
#                 basename = 'exit',
#                 )


#Где-то здесь или во view ошибка, найти