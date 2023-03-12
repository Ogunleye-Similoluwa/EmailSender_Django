from django.contrib.auth.models import User
from django.db import models


class Email(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_emails')
    subject = models.CharField(max_length=100)
    body = models.TextField()
