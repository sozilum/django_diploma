from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, \
                                        IsAuthenticated,
                                        )
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


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        body = json.loads(request.body)
        username = body['username']
        password = body['password']
        user = authenticate(request = request,
                            username = username,
                            password = password,
                            )
        
        if user is not None:
            login(request = request,
                  user = user,
                  )
            return HttpResponse(status = 200)
        
        else:
            return HttpResponse(status = 500)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        body = json.loads(request.body)
        user = User.objects.create_user(fullName = body['name'],
                                        username = body['username'],
                                        password = body['password'],
                                        )
        user.save()
        return HttpResponse(status = 200)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return HttpResponse(status = 200)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = Profile.objects.get(user_id = request.user.pk)
        profile_serializer = ProfileSerializer(user)
        return JsonResponse(profile_serializer.data)
    
class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        body = json.loads(request.body)
        user = Profile.objects.get(user_id = request.user.pk)
        
        user.fullName = body['fullName']
        user.phone = body['phone']
        user.email = body['email']

        user.save()

        return HttpResponse(status = 200)


class UpdatePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return HttpResponse(status = 200)

class UpdateAvatarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.FILES['avatar']
        return HttpResponse(status = 200)