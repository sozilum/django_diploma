from rest_framework import serializers

from .models import (Profile,
                     AvatarProfile,
                     )


class AvatarProfileSerializer(serializers.Serializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = AvatarProfile
        fields = [
            'src',
            'alt',
        ]
    
    def get_src(self, obj):
        return obj.src.url


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