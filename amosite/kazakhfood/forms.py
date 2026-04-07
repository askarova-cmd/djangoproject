from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'date', 'time', 'people_count']

        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'date': 'Дата',
            'time': 'Время',
            'people_count': 'Количество гостей',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите имя'
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': '+7 777 123 45 67'
            }),

            'date': forms.DateInput(attrs={
                'type': 'date'
            }),

            'time': forms.TimeInput(attrs={
                'type': 'time'
            }),

            'people_count': forms.NumberInput(attrs={
                'min': 1,
                'placeholder': 'Например: 4'
            }),
        }