from django.db import models
from django.contrib.auth.models import User


class BloodRequest(models.Model):

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    URGENCY_CHOICES = [
        ('NORMAL', 'Normal'),
        ('URGENT', 'Urgent'),
        ('EMERGENCY', 'Emergency'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blood_requests'
    )
    
    accepted_by = models.ForeignKey(
    'BloodVolunteer',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='accepted_requests'
    )

    patient_name = models.CharField(
        max_length=100
    )

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES
    )

    hospital = models.CharField(
        max_length=200
    )

    location = models.CharField(
        max_length=255
    )

    contact_number = models.CharField(
        max_length=15
    )

    units_required = models.PositiveIntegerField(
        default=1
    )

    urgency = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default='NORMAL'
    )

    description = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.patient_name} - {self.blood_group}"

class BloodVolunteer(models.Model):

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='blood_volunteer'
    )

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES
    )

    location = models.CharField(
        max_length=255
    )

    contact_number = models.CharField(
        max_length=15
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.blood_group}"    