# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.acquire_all_images()

    return render(request, 'home.html', {'images': images})

def registration(request):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email = form.cleaned_data.get('email')
                activation_email(user, current_site, email)
                return HttpResponse('Complete registration by confirming your email address')
        else:
            form = SignupForm()
        return render(request, 'registration/registration_form.html', {'form': form})