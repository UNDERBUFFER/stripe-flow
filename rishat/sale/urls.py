from django.urls import path
from sale.views import BuyItemView, ItemDetailView

urlpatterns = [
    path('item/<pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('buy/<pk>/', BuyItemView.as_view(), name='buy-item'),
]