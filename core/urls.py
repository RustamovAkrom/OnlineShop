from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy  as _
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.payment import webhooks


urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path(_('cart/'), include('apps.cart.urls', namespace='cart')),
    path(_('orders/'), include('apps.orders.urls', namespace='orders')),
    path(_('payment/'), include('apps.payment.urls', namespace='payment')),
    path(_('coupons/'), include('apps.coupons.urls', namespace='coupons')),
    path('rosetta/', include('rosetta.urls')),
    path('', include('apps.shop.urls', namespace='shop')),
)

urlpatterns += [
    path('webhook/', webhooks.stripe_webhook, name='stripe-webhook'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )