from django.shortcuts import render,redirect
from .forms import PatientRegisterForm,PatientProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponse
# Create your views here.
def registerpatient(request):
	if(request.method == 'POST'):
		form = PatientRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Account Created.')
			return redirect('login')

	else:
		form = PatientRegisterForm()
	return render(request, 'accounts/patient_registration.html',{'form':form})

def patientprofile(request):
	if(request.method == 'POST'):
		pform = PatientProfileUpdateForm(request.POST)
		if pform.is_valid():
			with connection.cursor() as cursor:
				cursor.execute("INSERT INTO patient (patientid,firstname) VALUES (8573,'firstnamel');")
		return redirect('patientprofile')
	else:
		pform = PatientProfileUpdateForm()
	return render(request, 'accounts/patient_profile.html',{'pform':pform})




	
def commit(request):
	with connection.cursor() as cursor:
	        cursor.execute("commit");
	return HttpResponse('')           

	       