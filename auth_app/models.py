from django.contrib.auth.models import User
from django.db import models


def profile_image_downloader(instance:'Profile', filename: str) -> str:
    return 'profile/profile_{pk}/{filename}'.format(pk = instance.pk,
                                                    filename = filename,
                                                    )


#Описание модели пользователя
class Profile(models.Model):
    class Meta:
        pass

    user = models.OneToOneField(User,
                                on_delete = models.CASCADE,
                                )
    avatar = models.ImageField(null = True, 
                               blank = True,
                               upload_to = profile_image_downloader,
                               )
    fullName = models.CharField(max_length = 100, 
                                  db_index = True,
                                  )
    phone = models.CharField(max_length = 11,
                            db_index = True,
                            )
    email = models.CharField(max_length = 100, 
                            db_index = True,
                            )
    
    def __str__(self) -> str:
        return self.fullName