from datetime import datetime
from django.db import models
from users.serializers import UserModel

class Post(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now) 

    def __str__(self):
        return self.text