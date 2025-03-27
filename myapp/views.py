from django.shortcuts import render
from rest_framework import generics
from .serializer import UserSerializer , CustomerSerializer , UserMessageSerializer
from django.contrib.auth.models import User 
from .models import CustomerInfo , UserMessages
from rest_framework.permissions import AllowAny  , IsAuthenticated , IsAdminUser
# Create your views here.

#creates  User
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

# lists all the users that has been created
class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Users message

# view for user message and images
class CreateUserMessageView(generics.CreateAPIView):
    queryset = UserMessages.objects.all()
    serializer_class= UserMessageSerializer
    permission_classes = [IsAuthenticated]

# lists all the user messages but cant delete and update
class ListUserMessageView(generics.ListAPIView):
    serializer_class = UserMessageSerializer
    permission_classes = [IsAuthenticated]

# this view will retrieve a single UserMessage instead of listing it all
class EditUserMessageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserMessageSerializer
    permission_classes = [IsAuthenticated]


# customer

# created customers request
class CreateCustomerInfoView(generics.CreateAPIView):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

# creates all the request that the customers has created
class ListCustomerInfoView(generics.ListAPIView):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
