from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateUserView ,ListUserView,CreateCustomerInfoView,ListCustomerInfoView, CreateUserMessageView, ListUserMessageView , EditUserMessageView

from django.urls import path , include

urlpatterns = [
    path('user/register/' , CreateUserView.as_view() , name = 'register'),

    path('user/all/' , ListUserView.as_view() , name = 'list_users'),
    path('user/customer/' ,CreateCustomerInfoView.as_view() , name = 'create_customer'),
    path('user/customer/info/' , ListCustomerInfoView.as_view() , name = 'list_customer_info'),
    path('user/message/', CreateUserMessageView.as_view(), name='todo'),
    path('user/message/list/',ListUserMessageView.as_view(), name='todo'),
    path('user/message/edit/<int:pk>/',  EditUserMessageView.as_view(), name='edit_todo')
]
