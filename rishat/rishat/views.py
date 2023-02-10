from django.http import HttpResponse

def response200(*args, **kwargs):
    return HttpResponse('success')

