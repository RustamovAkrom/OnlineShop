THIRD_PARTY_APPS = [
    "django_celery_results",
    "django_celery_beat",
    "rosetta",
    "modeltranslation",
    "localflavor",
    "ckeditor",
    "debug_toolbar",
]

DEFAULT_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.shop.apps.ShopConfig",
    "apps.shared.apps.SharedConfig",
    "apps.cart.apps.CartConfig",
    "apps.orders.apps.OrdersConfig",
    "apps.payment.apps.PaymentConfig",
    "apps.coupons.apps.CouponsConfig",
]
