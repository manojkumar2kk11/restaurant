from django.contrib import admin

# Register your models here.
from .models import Reservation, Menu
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass
