# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'base.html')


def top_view(request):
    return render(request, 'top.html')


def left_view(request):
    return render(request, 'left.html')


def down_view(request):
    return render(request, 'down.html')