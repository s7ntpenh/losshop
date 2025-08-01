from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('stripe/success/', views.stripe_success, name='stripe_success'),
    path('stripe/cancel/', views.stripe_cancel, name='stripe_cancel'),
    path('download/<str:session_id>/', views.download_view, name='order-download'),
]
