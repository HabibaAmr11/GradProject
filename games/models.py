from django.db import models
from users.models import User


class Game(models.Model):
    question = models.TextField()
    choice_a = models.TextField()
    choice_b = models.TextField()
    Choice_c = models.TextField()
    choice_d = models.TextField()
    correct_answer = models.TextField()
    created_by = models.ForeignKey(User, related_name='game_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
