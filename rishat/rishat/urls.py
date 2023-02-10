from django.contrib import admin
from django.urls import include, path
from rishat.views import response200


urlpatterns = [
    path('success', response200),
    path('admin/', admin.site.urls),
    path('', include('sale.urls')),
]
