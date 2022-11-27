from django.urls import path
from . import views
from .views import home_view,book_appointment_view,available_doctors_view,doctor_availability_view,successfully_booked_appointment_view,patient_medical_history_view,patient_views_appointment_view


urlpatterns = [
    path('',home_view,name = 'home'),
    path('bookappointment/',book_appointment_view,name = 'bookappointment'),
    path('patientappointment/',patient_views_appointment_view,name = 'patientappointment'),
    path('bookappointment/availabledoctors/',available_doctors_view,name = 'availabledoctors'),
    path('bookappointment/availabledoctors/doctoravailability',doctor_availability_view,name = 'doctoravailability'),
    path('bookappointment/availabledoctors/appointmentbookedsuccessfully',successfully_booked_appointment_view,name = 'appointmentbookedsuccessfully'),
    path('patientmedicalhistory/',patient_medical_history_view,name = 'patientmedicalhistory'),
]