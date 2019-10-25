
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from apps.core.views import(
    home
)

app_name='core'

urlpatterns = [
    path('', home, name='home'),
]
