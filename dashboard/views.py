from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple
import datetime
# Create your views here.
def home_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return render(request, 'dashboard/employeehome.html')
        

    else:
    	return render(request, 'dashboard/patienthome.html')


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
  
##should change the if condition because the patient can also see the payslip 
def payslip(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    else:
        current_user = request.user
        us = current_user.username
        with connection.cursor() as cursor:
            cursor.execute("select e.employeeID, firstname, lastname, designation, to_char(paymentdate, 'DD-MON-YYYY') as paymentdate, amount, deptid, paymentID from payslip p join employee e on p.employeeid = e.employeeid where e.employeeID = %s order by paymentdate",[us])
            query = dictfetchall(cursor)
            print(query)
        return render(request, 'dashboard/payslip.html',{'query' : query})


def docmedicalrecord(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    else:
        current_user = request.user
        us = current_user.username
        with connection.cursor() as cursor:
            cursor.execute("select e.employeeID, firstname, lastname, designation, to_char(paymentdate, 'DD-MON-YYYY') as paymentdate, amount, deptid, paymentID from payslip p join employee e on p.employeeid = e.employeeid where e.employeeID = %s order by paymentdate",[us])
            query = dictfetchall(cursor)
            print(query)
        return render(request, 'dashboard/payslip.html',{'query' : query})




def medical_record_view(request):
    # print(pform.instance.my_field)
    return render(request,'dashboard/docmedicalrecord.html') 
 
def medical_record_suc(request):
    print(request)
    if(request.method== 'POST'):
        diagnosis = request.POST["diagnosis"]
        knowndisease = request.POST['knowndisease']
        patientid = request.POST['patientid']
        print(diagnosis)
        print(knowndisease)
        current_user = request.user
        us = current_user.username
        with connection.cursor() as cursor:
             date = datetime.datetime.now().date()
             print(date)
             query = "INSERT into medical_record (diagnosis,knowndisease,patientid,recorddate) values (%s,%s,%s,%s)"
             cursor.execute(query, [diagnosis,knowndisease,patientid,date])
        return render(request, 'dashboard/medrecordsuccess.html')
            
def medrecordsearch(request):
    # print(pform.instance.my_field)
    return render(request,'dashboard/medrecordsearch.html') 

def medrecordview(request):
    print(request)
    if(request.method== 'GET'):
        patientid = request.GET['patientid']
        current_user = request.user
        us = current_user.username
        with connection.cursor() as cursor:
             date = datetime.datetime.now().date()
             print(date)
             cursor.execute("select p.patientID, firstname, lastname, age, gender, diagnosis, knowndisease from patient p join medical_record m on p.patientID = m.patientID where p.patientID = %s",[patientid])
             query = dictfetchall(cursor)
             print(type(query))
        return render(request, 'dashboard/medrecordview.html',{'query' : query})

def doctorappointments(request):
    current_user = request.user
    us = current_user.username
    with connection.cursor() as cursor:
        cursor.execute("select a.appid, firstname, lastname, age, gender, phoneno,  meetinglink, appointment_date, appointment_time from appointment a join patient p on a.patientid = p.patientid join online_appointment oa on a.appid = oa.appid WHERE employeeid = %s",[us])
        query = dictfetchall(cursor)
        cursor.execute("select a.appid, firstname, lastname, age, gender, phoneno,cabinno, appointment_date, appointment_time from appointment a join patient p on a.patientid = p.patientid join offline_appointment oa on a.appid = oa.appid WHERE employeeid = 'prav'")
        offquery = dictfetchall(cursor)
        print(offquery)
    return render(request, 'dashboard/doctorappointments.html',{'query' : query,'offquery':offquery})

