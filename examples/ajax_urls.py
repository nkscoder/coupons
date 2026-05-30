from django.urls import path, include
from coupons.ajax_views import *
from django.views.decorators.csrf import csrf_exempt 
urlpatterns = [
    path('coupon-apply/', csrf_exempt(Coupon_apply) , name='coupon-apply'),

]