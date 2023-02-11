import json
import stripe

from django.db.models import Count, F
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View as BaseView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from rishat.env import ENV
from sale.models import Item, Order, OrderItem


class ItemDetailView(DetailView):
    model = Item


class OrderView(ListView):
    model = Item

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order = None

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.order = None

        oid = request.session.get('oid', None)
        if oid is None:
            self.order = Order.objects.create()
            request.session['oid'] = self.order.pk
        else:
            self.order = Order.objects.get(id=oid)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.order.items.all() # type: ignore

    # def get(self, request, *args, **kwargs):
    #     items = [
    #         model_to_dict(i) for i in self.order.items.all()  # type: ignore
    #     ]
    #     return JsonResponse({
    #         'id': self.order.pk,  # type: ignore
    #         'data': json.dumps(items)
    #     })

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        if not json_data.get('id', None):
            return JsonResponse(
                {
                    'status': 'error',
                    'description': 'unknown id',
                }, status=403)

        item = Item.objects.get(id=json_data['id'])
        if not item.api_price_id:
            return JsonResponse(
                {
                    'status': 'error',
                    'description': 'empty api_price_id',
                },
                status=403)

        OrderItem.objects.create(order=self.order, item=item)  # type: ignore
        return JsonResponse({
            'status': 'ok',
            'id': self.order.pk,  # type: ignore
            'item_id': item.pk,
        })


class BuyOrderView(BaseView):
    model = Item

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        oid = request.session.get('oid', None)
        if oid is None:
            return JsonResponse(
                {
                    'status': 'error',
                    'description': 'empty cart',
                }, status=403)

        order = Order.objects.get(id=oid)
        items = order.items.all().exclude(api_price_id__isnull=True)

        if items.count() == 0:
            return JsonResponse(
                {
                    'status': 'error',
                    'description': 'empty cart',
                }, status=403)

        line_items = list(
            items.values('api_price_id').values(
                price=F('api_price_id')).annotate(quantity=Count('price')))

        id = stripe.checkout.Session.create(
            success_url=ENV['SUCCESS_PAYMENT_URL'],
            line_items=line_items,
            mode='payment').stripe_id

        return JsonResponse({
            'status': 'ok',
            'id': id,
        })
