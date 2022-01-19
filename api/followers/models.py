from django.db import models
from users.serializers import UserModel
from datetime import datetime

class Follower(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(default=datetime.now) 
    following_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='followings')