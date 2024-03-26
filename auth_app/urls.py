from .views import (AccountView,
                    ProfileView,
                    )

from django.urls import path


urlpatterns = [
    path('sing-in/', AccountView.post_login, name = 'log-in'),
    path('sign-up/', AccountView.post_register, name = 'register'),
    path('sign-out/', AccountView.post_logout, name = 'logout'),
    
    path('profile/', ProfileView.get_profile, name = 'profile'),
    path('profile/password/', ProfileView.update_password, name = 'update_password'),


]