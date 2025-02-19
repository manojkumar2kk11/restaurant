"""
URL configuration for dine_smart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from dine_smart.myrestaurant.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('accounts/', include('allauth.urls')),
    path('booktable/', book_table, name='booktable'),
    path('showbookings/', show_bookings, name='show_bookings'),
    path('menu/', show_menu, name='show_menu'),
    path('deletebooking/<int:entry_id>/', delete_booking, name='deletebooking'),
    path('modifybooking/<int:entry_id>/', modify_booking, name='modifybooking'),
    path('successbooking/', book_success, name='book_success' )
]
