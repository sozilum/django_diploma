from rest_framework.views import APIView
from django.contrib.auth import (authenticate,
                                 login,
                                 logout,
                                 )
from django.contrib.auth.models import User
from django.http import (HttpResponse,
                         JsonResponse,
                         )

from django.contrib.auth import authenticate

from .models import Profile
from .serializers import ProfileSerializer

import json


class AccountView(APIView):
    def post_login(self):
        body = json.loads(self.body)
        username = body['username']
        password = body['password']
        user = authenticate(request = self,
                            username = username,
                            password = password,
                            )
        
        if user is not None:
            login(request = self,
                  user = user,
                  )
            return HttpResponse(status = 200)
        
        else:
            return HttpResponse(status = 500)


    def post_register(self):
        body = json.loads(self.body)
        user = User.objects.create_user(fullName = body['name'],
                                        username = body['username'],
                                        password = body['password'],
                                        )
        user.save()
        return HttpResponse(status = 200)


    def post_logout(self):
        logout(self)
        return HttpResponse(status = 200)


class ProfileView(APIView):
    def get_profile(self):
        user = Profile.objects.get(user_id = self.user.pk)
        profile_serializer = ProfileSerializer(user)
        return JsonResponse(profile_serializer.data)
    

    def post_profile(self):
        body = json.loads(self.body)
        user = Profile.objects.get(user_id = self.user.pk)
        
        user.fullName = body['fullName']
        user.phone = body['phone']
        user.email = body['email']

        user.save()

        return HttpResponse(status = 200)


    def update_password(self):
        return HttpResponse(status = 200)


    def update_avatar(self):
        self.FILES['avatar']
        return HttpResponse(status = 200)
    

class PaymentView(APIView):
    def get_payment(self):
        pass