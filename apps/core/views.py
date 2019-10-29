# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def port_django_rest(request):
    return render(request, 'portfolio/django-rest.html')