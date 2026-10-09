from django.db import models
import uuid
from django.contrib.auth.models import User

class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name



class Complaint(models.Model):
    

    tracking_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
        )
    
    

    department = models.ForeignKey(
    Department,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='complaints'
)
    assigned_officer = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='assigned_complaints'
)
    
    CATEGORY_CHOICES = [
        ('GARBAGE', 'Garbage'),
        ('POTHOLE', 'Pothole'),
        ('STREETLIGHT', 'Streetlight'),
        ('WATER', 'Water Leakage'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('REJECTED', 'Rejected'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='complaints'
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    location = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to='complaints/',
        blank=True,
        null=True
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='MEDIUM'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    is_verified = models.BooleanField(
    default=False
)

    rejection_reason = models.TextField(
    blank=True
)

    duplicate_of = models.ForeignKey(
    'self',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='duplicate_complaints'
)

    updated_at = models.DateTimeField(
        auto_now=True
    )
    resolution_note = models.TextField(
    blank=True
)

    resolved_at = models.DateTimeField(
    null=True,
    blank=True
)

    citizen_feedback = models.TextField(
    blank=True
)

    citizen_rating = models.PositiveSmallIntegerField(
    null=True,
    blank=True
)

    def __str__(self):
        return self.title