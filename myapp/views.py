from django.shortcuts import render
from rest_framework import generics
from .serializer import UserSerializer , CustomerSerializer
from django.contrib.auth.models import User
from .models import CustomerInfo
from rest_framework.permissions import AllowAny  , IsAuthenticated
# Create your views here.

#creates Admin User
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CreateCustomerInfo(generics.CreateAPIView):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

class ListCustomerInfo(generics.ListAPIView):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
