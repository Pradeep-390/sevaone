
from django.contrib import admin

from .models import Complaint, Department


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    list_display = [
        'tracking_id',
        'title',
        'category',
        'department',
        'assigned_officer',
        'status',
        'priority',
        'created_at',
    ]

    list_filter = [
        'category',
        'department',
        'status',
        'priority',
    ]

    search_fields = [
        'tracking_id',
        'title',
        'description',
        'location',
    ]

    fieldsets = (

        ('Complaint Information', {
            'fields': (
                'user',
                'title',
                'description',
                'category',
                'location',
                'image',
                'priority',
            )
        }),

        ('Assignment', {
            'fields': (
                'department',
                'assigned_officer',
            )
        }),

        ('Verification & Status', {
            'fields': (
                'status',
                'is_verified',
                'rejection_reason',
                'duplicate_of',
            )
        }),

        ('Resolution', {
            'fields': (
                'resolution_note',
                'resolved_at',
            )
        }),

        ('Citizen Feedback', {
            'fields': (
                'citizen_feedback',
                'citizen_rating',
            )
        }),

        ('System Information', {
            'fields': (
                'tracking_id',
                'created_at',
                'updated_at',
            )
        }),

    )

    readonly_fields = [
        'tracking_id',
        'created_at',
        'updated_at',
    ]

    def get_form(self, request, obj=None, **kwargs):

        form = super().get_form(
            request,
            obj,
            **kwargs
        )

        if obj:

            possible_duplicates = Complaint.objects.filter(
                category=obj.category,
                location__iexact=obj.location
            ).exclude(
                pk=obj.pk
            )

            form.base_fields['duplicate_of'].help_text = (
                "Possible duplicates are complaints with "
                "the same category and location. "
                "Suggested matches: "
                + ", ".join(
                    str(complaint)
                    for complaint in possible_duplicates
                )
                if possible_duplicates.exists()
                else
                "No possible duplicates found."
            )

        return form


admin.site.register(Department)

