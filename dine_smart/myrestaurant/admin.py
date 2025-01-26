from django.contrib import admin
from .models import Reservation, Menu
# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass
