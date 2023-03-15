from django.db import models
from users.models import User
from museums.models import Museum


class Event(models.Model):
    museum = models.ForeignKey(Museum, related_name='event_museum', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()
    address = models.TextField()
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)
    created_by = models.ForeignKey(User, related_name='event_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Tour(models.Model):
    museum = models.ForeignKey(Museum, related_name='tour_museum', on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)
    created_by = models.ForeignKey(User, related_name='tour_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class BookTour(models.Model):
    user = models.ForeignKey(User, related_name='book_tour_user', on_delete=models.CASCADE)
    tour = models.ForeignKey(Museum, related_name='book_tour', on_delete=models.CASCADE)
    amount = models.IntegerField()
    QRCode = models.ImageField(upload_to='images')


class BookTicket(models.Model):
    user = models.ForeignKey(User, related_name='book_ticket_user', on_delete=models.CASCADE)
    museum = models.ForeignKey(Museum, related_name='book_ticket_museum', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)
    no_visitors = models.IntegerField()
    no_students = models.IntegerField()
    amount = models.IntegerField()
    qr_code = models.ImageField(upload_to='images')
