from django.shortcuts import render
from django.contrib.auth import login, logout
from rest_framework import permissions
from rest_framework import views, status
from rest_framework.response import Response
from . import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class LoginView(views.APIView):
  
   permission_classes = (permissions.AllowAny,)

    
   def post(self, request, format=None):
       serializer = serializers.LoginSerializer(data=self.request.data,context={ 'request': self.request })
    
       serializer.is_valid(raise_exception=True)
       user = serializer.validated_data['user']
       password = serializer.validated_data['password']
       print(user)
       print(password)
       login(request, user,password)
       return Response(None, status=status.HTTP_202_ACCEPTED)



class LogoutView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        logout(request)
        response = Response(None, status=status.HTTP_204_NO_CONTENT)
        response.set_cookie('sessionid',max_age=1,samesite='None')
        response.set_cookie('csrftoken',max_age=1,samesite='None')
        return response

class ProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.LoginSerializer

    def get_object(self):
        return self.request.user