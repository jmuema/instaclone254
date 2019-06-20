# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.acquire_all_images()

    return render(request, 'home.html', {'images': images})
