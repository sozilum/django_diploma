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
    path('sign-in/', LoginView.post_login, name = 'log-in'),
    path('sign-up/', RegisterView.post_register, name = 'register'),
    path('sign-out/', LogoutView.post_logout, name = 'logout'),
    
    path('profile/', ProfileView.get_profile, name = 'profile'),
    path('profile/', UpdateProfileView.post_profile, name = 'update_profile'),
    path('profile/password/', UpdatePasswordView.update_password, name = 'update_password'),
    path('profile/avatar/', UpdateAvatarView.update_avatar, name = 'avatar'),
]