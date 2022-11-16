from django.db import models

class Role(models.TextChoices):
    ADMIN = 'admin'
    REGULAR = 'regular'

class Member(models.Model):
    userId = models.IntegerField(blank=False, primary_key=True)
    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=45, default='')
    emailId = models.CharField(max_length=200, default='')
    role = models.CharField(max_length=45, choices=Role.choices, default=Role.REGULAR)
# Create your models here.
