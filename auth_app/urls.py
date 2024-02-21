from django.urls import (path,
                        include,
                        )
from django.contrib.auth.views import (LogoutView,
                                       LoginView,
                                       )

from rest_framework.routers import BaseRouter


# urlpatterns = [
#     path('',
#         include(router.urls),
#         )
# ]

#sign-in - вход
#sign-up - регистрация