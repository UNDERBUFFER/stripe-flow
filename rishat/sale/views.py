import stripe
from django.http import JsonResponse
from django.views.generic.detail import DetailView

from rishat.env import ENV
from sale.models import Item


class ItemDetailView(DetailView):
    model = Item


class BuyItemView(DetailView):
    model = Item

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.api_price_id is None: # type: ignore
            return JsonResponse(
                {
                    'status': 'error',
                    'description': 'empty api_price_id',
                },
                status=403
            )

        id = stripe.checkout.Session.create(
            success_url=ENV['SUCCESS_PAYMENT_URL'],
            line_items=[
                {
                    "price": self.object.api_price_id, # type: ignore
                    "quantity": 1,
                }
            ],
            mode='payment'
        ).stripe_id
        return JsonResponse(
            {
                'status': 'ok',
                'id': id,
            }
        )
