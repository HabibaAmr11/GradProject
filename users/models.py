from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    redeem_points = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.ForeignKey('self', related_name='user', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class ContactUs(models.Model):
    user = models.ForeignKey(User, related_name='contact_us_user', on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
