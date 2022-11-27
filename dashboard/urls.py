from django.urls import path
from . import views
from .views import home_view,book_appointment_view,available_doctors_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home_view,name = 'home'),
    path('bookappointment/',book_appointment_view,name = 'bookappointment'),
    path('bookappointment/availabledoctors/',available_doctors_view,name = 'availabledoctors'),

   
    
]