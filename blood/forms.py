from django import forms
from .models import BloodRequest,BloodVolunteer


class BloodRequestForm(forms.ModelForm):

    class Meta:
        model = BloodRequest

        fields = [
            'patient_name',
            'blood_group',
            'hospital',
            'location',
            'contact_number',
            'units_required',
            'urgency',
            'description',
        ]

        widgets = {

            'patient_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter patient name'
                }
            ),

            'blood_group': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'hospital': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter hospital name'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter hospital/location'
                }
            ),

            'contact_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter contact number'
                }
            ),

            'units_required': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1
                }
            ),

            'urgency': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Enter additional information'
                }
            ),
        }

class BloodVolunteerForm(forms.ModelForm):

    class Meta:
        model = BloodVolunteer

        fields = [
            'blood_group',
            'location',
            'contact_number',
            'is_available',
        ]

        widgets = {

            'blood_group': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your location'
                }
            ),

            'contact_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your contact number'
                }
            ),

            'is_available': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
        }        