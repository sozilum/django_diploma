from .views import (LoginView,
                    RegisterView,
                    LogoutView,
                    ProfileView,
                    UpdateProfileView,
                    UpdatePasswordView,
                    UpdateAvatarView,
                    )

from django.urls import path


urlpatterns = [
    path('sign-in/', LoginView.as_view(), name = 'log-in'),
    path('sign-up/', RegisterView.as_view(), name = 'register'),
    path('sign-out/', LogoutView.as_view(), name = 'logout'),
    
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('profile/', UpdateProfileView.as_view(), name = 'update_profile'),
    path('profile/password/', UpdatePasswordView.as_view(), name = 'update_password'),
    path('profile/avatar/', UpdateAvatarView.as_view(), name = 'avatar'),
]