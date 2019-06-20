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

def confirm(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        return HttpResponse('Successful. Feel free to log into your account.')

    else:
        return HttpResponse('Invalid')