from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    department = models.ForeignKey(
    'complaints.Department',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='officers'
    )

    ROLE_CHOICES = [
        ('CITIZEN', 'Citizen'),
        ('VOLUNTEER', 'Volunteer'),
        ('OFFICER', 'Officer'),
        ('ORGANIZATION', 'Organization'),
        ('ADMIN', 'Admin'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='CITIZEN'
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.user.username