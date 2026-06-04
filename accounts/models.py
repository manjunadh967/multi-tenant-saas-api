from django.db import models
from django.contrib.auth.models import AbstractUser
from organizations.models import Organization

class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]

    role = models.CharField(
    max_length=20,
    choices=ROLE_CHOICES,
    default='member'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    


