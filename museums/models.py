from django.db import models
from users.models import User


class Museum(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')
    location = models.TextField()
    created_by = models.ForeignKey(User, related_name='museum_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Collection(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()
    question_1 = models.TextField()
    answer_1 = models.TextField()
    question_2 = models.TextField()
    answer_2 = models.TextField()
    question_3 = models.TextField()
    answer_3 = models.TextField()
    link = models.TextField()
    museum = models.ForeignKey(Museum, related_name='collection_museum', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='collection_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Timeline(models.Model):
    photo = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False)
    created_by = models.ForeignKey(User, related_name='timeline_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorite_user', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, related_name='favorite_collection', on_delete=models.CASCADE)
