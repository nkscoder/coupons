# Coupons — Django Coupon & Discount Code System

[![PyPI version](https://badge.fury.io/py/coupons.svg)](https://pypi.org/project/coupons/)
[![Python](https://img.shields.io/pypi/pyversions/coupons.svg)](https://pypi.org/project/coupons/)
[![Django](https://img.shields.io/badge/Django-3.2%2B-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Author:** [Nitesh Kumar Singh](https://github.com/nkscoder) · **GitHub:** [@nkscoder](https://github.com/nkscoder)

A reusable **Django coupons app** for managing promotional codes, discount rules, and coupon validation in Python web applications. Built by **Nitesh Kumar Singh (nkscoder)** for e-commerce, SaaS, and any Django project that needs flexible coupon functionality.

> **Keywords:** django coupons · python coupon system · discount code · promo code · coupon validation · nkscoder · nitesh kumar singh

---

## Features

- **Percentage or fixed-amount discounts** on any order total
- **User-specific or global coupons** — restrict codes to selected users or allow all
- **Usage limits** — max total uses, uses per user, or unlimited
- **Expiration & active/inactive rules** with datetime-based validity
- **Django Admin integration** with bulk actions (reset usage, delete expired)
- **Simple validation API** — one function call to check any coupon code
- **Configurable coupon code length** via `DSC_COUPON_CODE_LENGTH` setting

---

## Requirements

- Python 3.8+
- Django 3.2+

---

## Installation

### From PyPI (recommended)

```bash
pip install coupons
```

### From GitHub

```bash
pip install git+https://github.com/nkscoder/coupons.git
```

---

## Setup

### Step 1 — Add to `INSTALLED_APPS`

```python
# settings.py
INSTALLED_APPS = [
    ...
    "coupons",
]
```

### Step 2 — Run migrations

```bash
python manage.py migrate coupons
```

### Step 3 — Create coupons in Django Admin

Go to `/admin/` and create:

1. **Discount** — set value and type (percentage or fixed)
2. **Allowed Users Rule** — select users or enable "All users"
3. **Max Uses Rule** — set limits or enable infinite uses
4. **Validity Rule** — set expiration date and active status
5. **Ruleset** — link the three rules above
6. **Coupon** — assign discount and ruleset (code auto-generated)

### Step 4 (optional) — Custom coupon code length

```python
# settings.py
DSC_COUPON_CODE_LENGTH = 16  # default is 12
```

---

## Usage

### Validate a coupon

```python
from coupons.validations import validate_coupon

coupon_code = "COUPONTEST01"
user = User.objects.get(username="nitesh")

status = validate_coupon(coupon_code=coupon_code, user=user)
# {'valid': True}

if status["valid"]:
    print("Coupon is valid!")
else:
    print(status["message"])  # e.g. "Coupon does not exist!"
```

### Apply a coupon (record usage)

```python
from coupons.models import Coupon

coupon = Coupon.objects.get(code=coupon_code)
coupon.use_coupon(user=user)
```

### Get discount details

```python
coupon = Coupon.objects.get(code=coupon_code)
discount = coupon.get_discount()
# {'value': 50, 'is_percentage': True}
```

### Calculate discounted price

```python
discounted = coupon.get_discounted_value(initial_value=100.0)
# Returns 50.0 for 50% off, or 80.0 for $20 off
```

---

## Validation Rules

| Rule | Description |
|------|-------------|
| **Allowed Users** | Coupon valid only for selected users, or all users |
| **Max Uses** | Global usage cap, per-user limit, or infinite |
| **Validity** | Active flag + expiration datetime |

Invalid responses include a human-readable `message` key:

```python
validate_coupon("DUMMYCODE", user)
# {'valid': False, 'message': 'Coupon does not exist!'}
```

---

## REST API Example

See [`examples/`](examples/) for a Django REST Framework integration sample (`ajax_views.py`, `ajax_urls.py`).

---

## Development

```bash
git clone git@github.com:nkscoder/coupons.git
cd coupons
pip install -e ".[dev]"
python manage.py migrate
python manage.py runserver
```

### Build & publish to PyPI

```bash
pip install build twine
python -m build
twine upload dist/*
```

Or tag a release on GitHub — the included GitHub Action publishes automatically.

---

## Changelog

### 1.1.0
- Modernized for Django 3.2–5.x and Python 3.8+
- Added PyPI packaging (`pyproject.toml`)
- Fixed per-coupon usage validation bug
- Fixed template mutation in validation responses
- SEO & documentation update by **Nitesh Kumar Singh (nkscoder)**

### 1.0.0
- Initial release

---

## Author & Links

| | |
|---|---|
| **Author** | Nitesh Kumar Singh |
| **GitHub** | [github.com/nkscoder](https://github.com/nkscoder) |
| **Repository** | [github.com/nkscoder/coupons](https://github.com/nkscoder/coupons) |
| **PyPI** | [pypi.org/project/coupons](https://pypi.org/project/coupons) |

---

## License

MIT License — Copyright (c) 2020-2026 [Nitesh Kumar Singh (nkscoder)](https://github.com/nkscoder)
