from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import (authenticate,
                                 login,
                                 logout,
                                 )
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

import json
from .models import Profile

class SignUpView(APIView):

    def post(self, request):
        serialized_data = list(request.POST.keys())[0]
        user_data = json.loads(serialized_data)
        name = user_data.get('name')
        username = user_data.get('username')
        password = user_data.get('password')

        try:
            user = User.objects.create_user(username = username,
                                            password = password,
                                            )
            profile = Profile.objects.create(user = user,
                                                name = name,
                                                )
            if user != None:
                login(request = request,
                        user = user,
                        )
            return Response(status = status.HTTP_201_CREATED)    
        except:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_extra_actions():
        return list()

# class SignInView(APIView):
#     @action(methods = ['post'],
#             detail = False
#             )
#     def login(self, request):
#         serialized_data = list(request.POST.keys())[0]
#         user_data = json.loads(serialized_data)
#         username = user_data.get('username')
#         password = user_data.get('password')

#         user = authenticate(request = request,
#                             username = username,
#                             password = password,
#                             )
        
#         if user != None:
#             login(request = request,
#                   user = user,
#                   )
#             return Response(status = status.HTTP_201_CREATED)

#         return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    


# class LogoutView(APIView):
#     @action(methods = ['post'],
#             detail = False,
#             )
#     def logout(self, request):
#         logout(request = request)
#         return HttpResponse(status = 200)


# class ProfileView():
#     def get()