from django import forms
from . models import Patient
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PatientRegisterForm(UserCreationForm) :
	
	
	class Meta:
		model = User
		fields = ['username','password1','password2']


class PatientProfileUpdateForm(forms.ModelForm) :
	
	class Meta:
		model = Patient
		fields = ['firstname']