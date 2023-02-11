from datetime import datetime
from django.http import HttpRequest
from sale.models import Order


def set_session_order(request: HttpRequest):
    order = None
    oid = request.session.get('oid', None)

    if oid is None:
        order = Order.objects.create()
        request.session['oid'] = order.pk
    else:
        order = Order.objects.get(id=oid)

    return order


def close_session_order(request: HttpRequest, order: Order):
    del request.session['oid']
    order.closed_at = datetime.now()
    order.save()
