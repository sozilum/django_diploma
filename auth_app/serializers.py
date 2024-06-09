from rest_framework import serializers

from .models import (Profile,
                     AvatarProfile,
                     )


class AvatarProfileSerializer(serializers.Serializer):
    class Meta:
        model = AvatarProfile
        fields = [
            'src',
            'alt',
        ]


class ProfileSerializer(serializers.ModelSerializer):
    avatar = AvatarProfileSerializer()

    class Meta:
        model = Profile
        fields = [
            'user',
            'avatar',
            'fullName',
            'phone',
            'email',
        ]