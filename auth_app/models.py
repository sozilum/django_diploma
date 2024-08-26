from django.contrib.auth.models import User
from django.db import models


def profile_image_downloader(instance: 'Profile', filename: str) -> str:
    return 'profile/{filename}'.format(filename=filename)


class AvatarProfile(models.Model):
    class Meta:
        pass

    src = models.ImageField(upload_to=profile_image_downloader,
                            null=True,
                            blank=True,
                            )
    alt = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.alt


class Profile(models.Model):
    class Meta:
        pass

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                )
    avatar = models.ForeignKey(AvatarProfile,
                               on_delete=models.CASCADE,
                               null=True,
                               )
    fullName = models.CharField(max_length=100,
                                db_index=True,
                                )
    phone = models.CharField(max_length=11,
                             db_index=True,
                             )
    email = models.CharField(max_length=100,
                             db_index=True,
                             )

    def __str__(self) -> str:
        return self.fullName
