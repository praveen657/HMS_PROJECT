from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple
from django.utils import timezone
import datetime
from datetime import date
from django.utils.dateparse import parse_date

# Create your views here.
def home_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return HttpResponse('')
        

    else:
    	current_user = request.user
    	us = current_user.username
    	with connection.cursor() as cursor:
	        cursor.execute("with pivoted_paitent_bill as (select * from (select * from patient_bill pb) pivot (sum(pbamount) for PBStatus in ('Paid' as Patient_Bill_Paid, 'Pending' as Patient_Bill_Pending))),patient_all_bills as (select patientid, coalesce(sum(Patient_Bill_Paid), 0) as Bill_paid, coalesce(sum(Patient_Bill_Pending), 0) as Bill_Due from pivoted_paitent_bill group by patientid) select p.PatientID, firstname, lastname, age, phoneno, Bill_Paid, Bill_Due, (Bill_Paid + Bill_Due) as Total_Bill from patient p join patient_all_bills pab on p.patientid = pab.patientid where p.patientID =%s;",[us])
	        query = dictfetchall(cursor)
	        print(query)
    	return render(request, 'dashboard/patienthome.html',{'query':query})


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def book_appointment_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return HttpResponse('')
        

    else:
    	with connection.cursor() as cursor:
	        cursor.execute("select distinct DEPTNAME FROM DEPARTMENT")
	        query = dictfetchall(cursor)

	        return render(request, 'dashboard/bookanappointment.html',{'query': query})
    

def available_doctors_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return HttpResponse('')
        

    else:
    	result = request.GET["departments"]
    	print(type(result))
    	with connection.cursor() as cursor:
	        cursor.execute("SELECT employeeID, firstname,lastname, deptname FROM employee e JOIN department d ON e.deptID = d.deptID WHERE designation = 'Doctor' and deptname = %s ORDER BY deptname, employeeID, firstname, lastname",[result])
	        query = dictfetchall(cursor)

	    
    	
    	return render(request, 'dashboard/available_doctors.html',{'query' : query})
  

def doctor_availability_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return HttpResponse('')
        

    else:
    	today = date.today()

    	dates = []
    	for i in range(1,8):
    		tom = today + datetime.timedelta(days = i)
    		dates.append(datetime.datetime.strptime(str(tom), '%Y-%m-%d').strftime('%y/%m/%d'))
    		print(datetime.datetime.strptime(str(tom), '%Y-%m-%d').strftime('%y/%m/%d'))



    	result2 = request.GET["employeeid"]

    	print(result2)
    	print(type(result2))
    	
    	

	    
    	
    	return render(request, 'dashboard/doctor_availability.html',{'dates':dates,'result2':result2})


def successfully_booked_appointment_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return HttpResponse('')
        

    else:
    	current_user = request.user
    	us = current_user.username
    	result2 = request.GET.get("employeeid")
    	date = request.GET.get("dates")

    	time = request.GET["time"]
    	onlineoffline = request.GET["onlineoffline"]
    	print(onlineoffline)
    	print(type(onlineoffline))
    	print(date)
    	print(type(date))
    	print(result2)
    	with connection.cursor() as cursor:
	        query = "INSERT INTO appointment (patientID, appointment_time, appointment_date, type, employeeid) VALUES (%s,%s,%s,%s,%s)"
	        cursor.execute(query,[us,time,date,onlineoffline,result2])
    	
    		
	        
    	
    	return render(request, 'dashboard/appointmentbookedsuccessfully.html')



def patient_medical_history_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return HttpResponse('')
        

    else:
    	current_user = request.user
    	us = current_user.username
    	with connection.cursor() as cursor:
	        cursor.execute("select p.patientID, firstname, lastname, age, gender, diagnosis, knowndisease from patient p join medical_record m on p.patientID = m.patientID where p.patientID = %s",[us])
	        query = dictfetchall(cursor)

    	
    	
    	

	    
    	print(query)
    	return render(request, 'dashboard/patientmedicalhistory.html',{'query':query})


def patient_views_appointment_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return HttpResponse('')
        

    else:
    	current_user = request.user
    	us = current_user.username
    	with connection.cursor() as cursor:
	        # cursor.execute("select firstname, lastname, email, meetinglink, appointment_date,appointment_time from appointment a join employee e on a.employeeid = e.employeeid join online_appointment oa on a.appid = oa.appid WHERE patientid = %s",[us])
	        cursor.execute("select firstname, lastname, email, meetinglink, to_char(appointment_date, 'DD-MON-YYYY') as appdate,appointment_time from appointment a join employee e on a.employeeid = e.employeeid join online_appointment oa on a.appid = oa.appid WHERE patientid = %s",[us])
	        query = dictfetchall(cursor)

    	
    	
    	

	    
    	print(query)
    	return render(request, 'dashboard/patientappointments.html',{'query':query})
