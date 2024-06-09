from django.contrib import admin
import pathlib
from .models import (Profile,
                     AvatarProfile,
                     )


@admin.register(AvatarProfile)
class AvatarProfileAdmin(admin.ModelAdmin):

    list_display = [
        'src',
        'alt',
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'avatar',
        'fullName',
        'phone',
        'email',
    ]