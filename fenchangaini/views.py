#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

def index(request):
    a = 1
    return render(request, 'index.html', locals())