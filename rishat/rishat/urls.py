from django.contrib import admin
from django.urls import include, path
from rishat.views import response200, echo


urlpatterns = [
    path('', echo),
    path('success/', response200),
    path('admin/', admin.site.urls),
    path('', include('sale.urls')),
]
