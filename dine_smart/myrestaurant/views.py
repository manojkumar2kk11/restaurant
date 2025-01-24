from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Reservation, Table, Menu
from dine_smart.myrestaurant.forms import ReserveForm
from datetime import *

# Create your views here.

def homepage(request):
    return render(request, 'home/home.html')

def booktable(request):
    return render(request, 'booktable/booktable.html', {'user': request.user})

def book_table(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            booked_date = form.cleaned_data['date']
            booked_time = form.cleaned_data['time']
            guests = form.cleaned_data['guests']

            booked_table = available_table(booked_date, booked_time, guests)

            if booked_table:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.table = booked_table
                reservation.save()
                return redirect('book_success')
            else:
                error_message = "There are no tables available for the chosen time and number of guests."
                return render(request, 'booktable/booktable.html', {'form': form, 'error_message': error_message})
    else:
        form = ReserveForm()
        

    return render(request, 'booktable/booktable.html', {'form': form})

def available_table(booked_date, booked_time, guests):
    available_tables = Table.objects.filter(table_guests__gte=guests)

    for table in available_tables:
        if not Reservation.objects.filter(table=table, date=booked_date, time=booked_time).exists():
            return table

    return None

def book_success(request):
    return render(request, 'successbooking/successbooking.html')

def show_bookings(request):
    user_bookings = Reservation.objects.filter(user=request.user)
    today = date.today()
    return render(request, 'showbooking/showbooking.html', {'user_bookings': user_bookings, 'today': today})


def show_menu(request):
    print("Menu page accessed")
    menu_items = Menu.objects.all()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})


def delete_booking(request, entry_id):
    entry = get_object_or_404(Reservation, pk=entry_id)

    if request.method == 'POST':
        entry.delete()
        return redirect('show_bookings')
    return render(request, 'deletebooking/deletebooking.html', {'entry': entry})


def modify_booking(request, entry_id):
    entry = get_object_or_404(Reservation, pk=entry_id)

    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=entry)

        if form.is_valid():
            form.save()
            return redirect('show_bookings')

    else:
        form = ReserveForm(instance=entry)

    return render(request, 'modifybooking/modifybooking.html', {'form': form})

