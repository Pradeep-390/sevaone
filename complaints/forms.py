from django import forms

from .models import Complaint


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            'title',
            'description',
            'category',
            'location',
            'image',
            'priority',
        ]


class ComplaintStatusForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            'status',
        ]
class ComplaintVerificationForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            'status',
            'rejection_reason',
        ]  
        
class ResolutionForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            'status',
            'resolution_note',
        ]  
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Complaint

        fields = [
            'citizen_feedback',
            'citizen_rating',
        ]

        widgets = {
            'citizen_feedback': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),
        }                    