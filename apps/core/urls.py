
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from apps.core.views import(
    home, port_django_rest
)

app_name='core'

urlpatterns = [
    path('', home, name='home'),
    path('port_django_rest', port_django_rest, name='django_rest'),
]
