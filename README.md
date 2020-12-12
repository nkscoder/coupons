# Coupons - Django
---
#### Description
Coupons project for 'Coupons' functionality is built in Python (Django)
#### Requirements
* **Python = 3.5.**
* Django = 1.11.5
* environ = 1.0
* pytz = 2017.2
### Configuration Instructions
* **Step 1:** Clone the Git Repository
  `git clone https://github.com/nkscoder/coupons.git`
* **Step 2:** CD into that directory

* **Step 3:** Run Migrations
 `python manage.py migrate`
* **Step 4:** Run Development Server
 `python manage.py runserver`


 * **Step 5:** Functionality for user-specific and common coupon
 `Use Coupon Code`

 `from .validations import validate_coupon`
  `from .models import Coupon`

  `coupon_code = "COUPONTEST01"`
  `user = User.objects.get(username="nitesh")`
  `status = validate_coupon(coupon_code=coupon_code, user=user)`
  `if status['valid']:`
    `coupon = Coupon.objects.get(code=coupon_code)`
    `coupon.use_coupon(user=user)`


`coupon_code = "COUPONTEST01"`
`coupon = Coupon.objects.get(code=coupon_code)`

`discount = coupon.get_discount()  # Example: {'value': 50, 'is_percentage': True} `


`coupon_code = "COUPONTEST01"`
`coupon = Coupon.objects.get(code=coupon_code)`

`''' Example: Returns 50.0 if discount is 50% or 80.0 if discount is $20 '''`
`discount_value = coupon.get_discounted_value(initial_value=100.0)`

* **Validations** *
`user = User.objects.get(username="nitesh")`
`coupon_code_valid = "COUPONTEST01"`

`valid = validate_coupon(coupon_code=coupon_code_valid, user=user)`
`# {'valid': True}`

`coupon_code_invalid = "DUMMYCOUPON0"`
`invalid = validate_coupon(coupon_code=coupon_code_invalid, user=user)`
`# {'valid': False, 'message': 'Coupon does not exist!'}`

