from django.http import HttpResponse

def response200(*args, **kwargs):
    return HttpResponse('success')

def echo(*args, **kwargs):
    return HttpResponse('hello world')