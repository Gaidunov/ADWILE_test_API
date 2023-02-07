from django.db import models
from django.contrib.auth.models import User


class Teaser(models.Model):

    """Teaser model"""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=64, choices=(("pending", "pending"), ("approved", "approved"), ("declined", "declined")))

    def __str__(self):
        return self.title

class Wallet(models.Model):

    """User Wallet Model"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):
        return f"{self.user} Wallet"