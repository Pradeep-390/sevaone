from django.contrib import admin
from .models import BloodRequest, BloodVolunteer


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):

    list_display = [
        'patient_name',
        'blood_group',
        'hospital',
        'location',
        'units_required',
        'urgency',
        'status',
        'created_at',
    ]

    list_filter = [
        'blood_group',
        'urgency',
        'status',
    ]

    search_fields = [
        'patient_name',
        'hospital',
        'location',
        'contact_number',
    ]


@admin.register(BloodVolunteer)
class BloodVolunteerAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'blood_group',
        'location',
        'contact_number',
        'is_available',
        'created_at',
    ]

    list_filter = [
        'blood_group',
        'is_available',
    ]

    search_fields = [
        'user__username',
        'location',
        'contact_number',
    ]