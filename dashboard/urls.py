from django.urls import path
from . import views
from .views import home_view,book_appointment_view,available_doctors_view, payslip,medical_record_view,medical_record_suc,medrecordsearch,medrecordview,doctorappointments
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home_view,name = 'home'),
    path('bookappointment/',book_appointment_view,name = 'bookappointment'),
    path('bookappointment/availabledoctors/',available_doctors_view,name = 'availabledoctors'),
    path('payslip/',payslip,name = 'payslip'),
    path('docmedicalrecord/',medical_record_view,name = 'docmedicalrecord'),
    path('docmedicalrecord/medrecordsuccess',medical_record_suc,name = 'medrecordsuccess'),
    path('medrecordsearch/',medrecordsearch,name = 'medrecordsearch'),
    path('medrecordsearch/medrecordview',medrecordview,name = 'medrecordview'),
    path('doctorappointments/',doctorappointments,name = 'doctorappointments'),
    #path('docmedicalrecord//medrecordssuccess',medical_record_success,name = 'docmedicalrecord'),
    # path('medrecordsuccess/',medical_record_view,name = 'medrecordsuccess'),,
    # path('docmedicalrecord/medrecordssuccess',medical_record,name = 'medrecordssuccess'),
    

   
    
]