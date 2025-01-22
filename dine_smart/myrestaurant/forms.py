from django.forms import ModelForm
from django import forms
from .models import Reservation
from django.forms.widgets import DateInput
from datetime import date


class FutureDateInput(DateInput):
    def __init__(self, attrs=None):
        super().__init__(attrs={'min': date.today().strftime('%Y-%m-%d'), **(attrs or {})})


class ReserveForm(ModelForm):
    Guests_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    ]

    TIME_CHOICES = [
        ('17:00', '17:00'),
        ('17:30', '17:30'),
        ('18:00', '18:00'),
        ('18:30', '18:30'),
        ('19:00', '19:00'),
        ('19:30', '19:30'),
        ('20:00', '20:00'),
        ('20:30', '20:30'),
        ('21:00', '21:00'),
        ('21:30', '21:30'),
        ('22:00', '22:00'),
    ]

    guests = forms.ChoiceField(
        choices=Guests_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            }),
    )

    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email',
                  'contact_number', 'date', 'time', 'guests']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', "required": True}),
            'contact_number': forms.NumberInput(attrs={'type': 'tel', 'class': 'form-control', "required": True}),
            'date': FutureDateInput(attrs={'type': 'date', 'class': 'form-control', "required": True}),
        }