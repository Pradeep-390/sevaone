from django import forms

from .models import FoodDonation, ItemDonation


class FoodDonationForm(forms.ModelForm):

    class Meta:
        model = FoodDonation

        fields = [
            'food_name',
            'food_type',
            'quantity',
            'description',
            'pickup_location',
            'available_from',
            'available_until',
        ]

        widgets = {
            'food_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Rice and Curry'
            }),

            'food_type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 20 meals'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter food details',
                'rows': 4
            }),

            'pickup_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pickup location'
            }),

            'available_from': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),

            'available_until': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }


class ItemDonationForm(forms.ModelForm):

    class Meta:
        model = ItemDonation

        fields = [
            'item_name',
            'item_type',
            'quantity',
            'description',
            'pickup_location',
            'available_from',
            'available_until',
        ]

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: School Books'
            }),

            'item_type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 10 books'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the items',
                'rows': 4
            }),

            'pickup_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pickup location'
            }),

            'available_from': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),

            'available_until': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }