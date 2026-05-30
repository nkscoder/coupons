from django.shortcuts import render
from .models import *
from core.models import *
from .validations import *
import json
from rest_framework.response import Response
from rest_framework import status as ss_status
from rest_framework.decorators import api_view, renderer_classes
# Create your views here.

@api_view(('POST',))
def Coupon_apply(request):
    product_id = request.POST.get('product_id', None)
    p_quantity = request.POST.get('p_quantity', None)
    coupon_code = request.POST.get('coupon_code', None)
    user_id = request.POST.get('user_id', None)

    if product_id==None or product_id=="" or  p_quantity==None or  p_quantity=="" or coupon_code==None or coupon_code=="" or user_id==None or user_id=="":
        return Response(data={"message": "Something went wrong"}, status=ss_status.HTTP_400_BAD_REQUEST)
    try:
        user = UserProfile.objects.get(user__id=user_id).user
        product = Product.objects.get(id=product_id)
        coupon = Coupon.objects.get(code=coupon_code)
        status = validate_coupon(coupon_code=coupon_code, user=user)
        if status['valid']:
            discount = coupon.get_discount()
            total_discount = discount['value']
            main_price = float(product.price)*float(p_quantity)
            save = total_discount/100*(main_price)
            total = round(main_price-save,2)

            return Response(data={"status": status['valid'],"message": f"Coupon Applied with {total_discount}% off and {round(save,2)}USD Save","price":total,"total_save":save}, status=ss_status.HTTP_200_OK)
        return Response(data={"status":"false","message": status['message']}, status=ss_status.HTTP_406_NOT_ACCEPTABLE)

    except Coupon.DoesNotExist:
        return Response(data={"status":"false","message": "Invalid Coupon Code"}, status=ss_status.HTTP_404_NOT_FOUND)
