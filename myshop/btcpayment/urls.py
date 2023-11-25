from django.urls import path
from . import views

app_name = 'payments_btc'

urlpatterns = [
    path('product_list/', views.home, name='home'),
    path('payments/create/<pk>', views.create_payment, name='create_payment'),
    path('payment/invoice/<pk>',views.track_invoice, name='track_payment'),
    path('payments/receive/', views.receive_payment, name='receive_payment'),
]

