from django.urls import path
from sale.views import CloseOrderAPIView, ItemDetailView, ItemListView, AddOrderItemAPIView

urlpatterns = [
    path('item/<pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('cart/', ItemListView.as_view(), name='cart-detail'),
    path('cart/add/', AddOrderItemAPIView.as_view(), name='cart-add'),
    path('cart/buy/', CloseOrderAPIView.as_view(), name='cart-buy'),
]