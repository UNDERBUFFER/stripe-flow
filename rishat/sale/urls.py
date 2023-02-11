from django.urls import path
from sale.views import BuyOrderView, ItemDetailView, OrderView

urlpatterns = [
    path('item/<pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('cart/', OrderView.as_view(), name='cart-detail'),
    path('cart/buy/', BuyOrderView.as_view(), name='cart-buy'),
]