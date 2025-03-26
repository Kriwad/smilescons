from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateUserView ,ListUserView,CreateCustomerInfo,ListCustomerInfo

from django.urls import path , include

urlpatterns = [
    path('user/register/' , CreateUserView.as_view() , name = 'register'),

    path('user/all/' , ListUserView.as_view() , name = 'list_users'),
    path('user/customer/' ,CreateCustomerInfo.as_view() , name = 'create_customer'),
    path('user/customer/info/' , ListCustomerInfo.as_view() , name = 'list_customer_info')
]
