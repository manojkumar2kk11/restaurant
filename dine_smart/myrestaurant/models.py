from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from djmoney.models.fields import MoneyField
from django.forms.widgets import DateInput
from datetime import date

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_guests = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number}"

    def can_accommodate(self, guests):
        return self.table_guests >= guests


def get_default_table():
    try:
        return Table.objects.get(table_number=1)
    except Table.DoesNotExist:
        return None  # Or you can raise an exception here if preferred


class FutureDateInput(DateInput):
    def __init__(self, attrs=None):
        super().__init__(attrs={'min': date.today().strftime('%Y-%m-%d'), **(attrs or {})})


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    contact_number = models.CharField(max_length=15, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    guests = models.IntegerField(null=False, blank=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=get_default_table)

    def __str__(self):
        return f"{self.date} | {self.time} | {self.table}"

    def clean(self):
        if self.table and not self.table.can_accommodate(self.guests):
            raise ValidationError(f"Table {self.table.table_number} cannot accommodate {self.guests} guests.")


class Menu(models.Model):
    menu_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=80, null=True, blank=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.menu_name