from django.db import models
from django.contrib.auth.models import User


class FoodDonation(models.Model):

    FOOD_TYPE_CHOICES = [
        ('COOKED_FOOD', 'Cooked Food'),
        ('PACKAGED_FOOD', 'Packaged Food'),
        ('GROCERIES', 'Groceries'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('COLLECTED', 'Collected'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    donor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='food_donations'
    )

    accepted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='accepted_food_donations'
    )

    food_name = models.CharField(
        max_length=200
    )

    food_type = models.CharField(
        max_length=30,
        choices=FOOD_TYPE_CHOICES
    )

    quantity = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    pickup_location = models.CharField(
        max_length=255
    )

    available_from = models.DateTimeField()

    available_until = models.DateTimeField()

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
        return f"{self.food_name} - {self.donor.username}"


class ItemDonation(models.Model):

    ITEM_TYPE_CHOICES = [
        ('CLOTHES', 'Clothes'),
        ('BOOKS', 'Books'),
        ('FURNITURE', 'Furniture'),
        ('SCHOOL_ITEMS', 'School Items'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('COLLECTED', 'Collected'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    donor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='item_donations'
    )

    accepted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='accepted_item_donations'
    )

    item_name = models.CharField(
        max_length=200
    )

    item_type = models.CharField(
        max_length=30,
        choices=ITEM_TYPE_CHOICES
    )

    quantity = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    pickup_location = models.CharField(
        max_length=255
    )

    available_from = models.DateTimeField()

    available_until = models.DateTimeField()

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
        return f"{self.item_name} - {self.donor.username}"