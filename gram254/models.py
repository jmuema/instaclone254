# -*- coding: utf-8 -*-
from django.db import models
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    
    profile_image = ImageField(null=True, blank=True)
    profile_bio = HTMLField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['user']

    def save_profile(self):
        self.save()

    @classmethod
    def profile_search(cls, tag):
        profile = Profile.objects.filter(user__username__icontains=tag)
        return profile

    @classmethod
    def acquire_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile
