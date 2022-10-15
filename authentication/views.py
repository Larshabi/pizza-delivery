from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import UserSerializer, EmailVerificationSerializer
from rest_framework.permissions import AllowAny
import jwt
from django.conf import settings
from .models import User
import requests

class UserCreateView(GenericAPIView):
    serializer_class = UserSerializer
    permission_class = [AllowAny]
    def post(self, request):
        data=request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyEmail(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = EmailVerificationSerializer
    
    def get(self, request, uid, token):
        post_url = "http://127.0.0.1:8000/auth/users/activation/"
        post_data = {"uid": uid, "token": token}
        result = requests.post(post_url, data=post_data)
        return Response({"message":"Account successfully activated"})