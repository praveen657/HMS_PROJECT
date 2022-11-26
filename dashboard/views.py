from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def home_view(request):
    if request.user.is_superuser:
        return HttpResponse('')
        
    if request.user.is_staff:
        return HttpResponse('')
        

    else:
    	return render(request, 'dashboard/patienthome.html')
