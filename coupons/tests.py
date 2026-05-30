from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from coupons.models import (
    AllowedUsersRule,
    Coupon,
    Discount,
    MaxUsesRule,
    Ruleset,
    ValidityRule,
)
from coupons.validations import validate_coupon


User = get_user_model()


class CouponValidationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.discount = Discount.objects.create(value=10, is_percentage=True)
        self.allowed = AllowedUsersRule.objects.create(all_users=True)
        self.max_uses = MaxUsesRule.objects.create(
            max_uses=100, is_infinite=False, uses_per_user=1
        )
        self.validity = ValidityRule.objects.create(
            expiration_date=timezone.now() + timedelta(days=30),
            is_active=True,
        )
        self.ruleset = Ruleset.objects.create(
            allowed_users=self.allowed,
            max_uses=self.max_uses,
            validity=self.validity,
        )
        self.coupon = Coupon.objects.create(
            code="TESTCODE1234",
            discount=self.discount,
            ruleset=self.ruleset,
        )

    def test_valid_coupon(self):
        result = validate_coupon("TESTCODE1234", self.user)
        self.assertTrue(result["valid"])

    def test_invalid_coupon_code(self):
        result = validate_coupon("NOTEXIST", self.user)
        self.assertFalse(result["valid"])
        self.assertEqual(result["message"], "Coupon does not exist!")

    def test_get_discounted_value_percentage(self):
        self.assertEqual(self.coupon.get_discounted_value(100.0), 90.0)

    def test_get_discounted_value_fixed(self):
        self.discount.is_percentage = False
        self.discount.value = 20
        self.discount.save()
        self.assertEqual(self.coupon.get_discounted_value(100.0), 80.0)
